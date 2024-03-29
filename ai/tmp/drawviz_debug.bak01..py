from graphviz import Digraph
import pprint

pp = pprint.PrettyPrinter(indent=4)


def trace(root):
    nodes, edges = set(), set()

    def build(v):
        if v not in nodes:
            nodes.add(v)
            for child in v._prev:
                edges.add((child, v))
                build(child)

    build(root)
    return nodes, edges


def draw_dot(root, debug_print_01=False):
    # print(root)

    dot = Digraph(format="svg", graph_attr={"rankdir": "LR"})  # LR = left to right

    nodes, edges = trace(root)
    for n in nodes:
        if debug_print_01:
            print(n)

        uid = str(id(n))
        # for any value in the graph, create a rectangular ('record') node for it
        dot.node(
            name=uid,
            label="{ %s |%s |%s |%s | data %.4f | grad %.4f }"
            % (n.name, n.layernumber, n.neuronnumber, n.type, n.data, n.grad),
            shape="record",
        )
        if n._op:
            # if this value is a result of some operation, create an op node for it
            dot.node(name=uid + n._op, label=n._op)
            # and connect this node to it
            dot.edge(uid + n._op, uid)

    for n1, n2 in edges:
        # connect n1 to the op node of n2
        dot.edge(str(id(n1)), str(id(n2)) + n2._op)

    return dot


def draw_nn(inputs, model, debug_print_01=False):
    nn_dot = Digraph(
        format="svg", node_attr={"shape": "record"}, graph_attr={"rankdir": "LR"}
    )  # LR = left to right

    with nn_dot.subgraph(name="cluster_I") as c:
        c.attr(label="I")
        c.attr(style="filled", color="lightgrey")
        c.node_attr.update(style="filled", color="white")
        for i in inputs:
            istring = "|{i |d %.4f g %.4f}" % (i.data, i.grad)
            c.node(
                "%s" % (i.type),
                r"  %s %s}" % (i.type, istring),
            )

    for l in model.layers:
        # print("layer %s" % l.layernumber)

        with nn_dot.subgraph(name="cluster_%s" % l.layernumber) as c:
            c.attr(label=l.layernumber)
            c.attr(style="filled", color="lightgrey")
            c.node_attr.update(style="filled", color="white")

            for n in l.neurons:
                # print("neuron %s" % n.neuronnumber)
                wstring = ""
                for w in n.w:
                    wstring += "|{%s |d %.4f g %.4f}" % (w.type, w.data, w.grad)
                # print(wstring)

                bstring = "|{b |d %.4f g %.4f}" % (n.b.data, n.b.grad)
                # print(bstring)

                astring = "|{a |d %.4f g %.4f}" % (n.act.data, n.act.grad)
                # print(astring)

                lstring = l.layernumber
                # print(model.sz)

                c.node(
                    "%s%s" % (lstring, n.neuronnumber),
                    r"  %s %s %s %s}" % (n.neuronnumber, wstring, bstring, astring),
                )

    for i in inputs:
        # print(i.type, i.data)
        # nn_dot.edge(i.type, "L1N1")
        for n in model.layers[0].neurons:
            nstring = "%s%s" % (model.layers[0].layernumber, n.neuronnumber)
            nn_dot.edge(i.type, nstring)
            if debug_print_01:
                # pp.pprint(nstring)
                print("edge input %s to %s" % (i.type, nstring))

    for thiselem, nextelem in zip(model.layers, model.layers[1:] + model.layers[:1]):
        # print(
        #     "this layer %s next layer %s" % (thiselem.layernumber, nextelem.layernumber)
        # )
        for n in thiselem.neurons:
            for m in nextelem.neurons:
                if nextelem.layernumber != "L1":
                    edge1 = "%s%s" % (thiselem.layernumber, n.neuronnumber)
                    edge2 = "%s%s" % (nextelem.layernumber, m.neuronnumber)
                    nn_dot.edge(edge1, edge2)
                    if debug_print_01:
                        print(
                            "edge neuron %s %s to %s" % (n.neuronnumber, edge1, edge2)
                        )
                        # print("%s to %s" % (edge1, edge2))

    return nn_dot


def print_my_params_old(model):
    # print(model.layers)

    for l in model.layers:
        print("layer %s" % l.layernumber)
        # pp.pprint(l.parameters())
        for n in l.neurons:
            print("neuron %s" % n.neuronnumber)
            # pp.pprint(n.parameters())
            for w in n.w:
                # print(w)
                print(
                    "layer %s neuron %s type %s data %.4f grad %.4f "
                    % (l.layernumber, w.neuronnumber, w.type, w.data, w.grad)
                )
            print(
                "layer %s neuron %s type %s data %.4f grad %.4f "
                % (l.layernumber, n.b.neuronnumber, n.b.type, n.b.data, n.b.grad)
            )


def print_my_params(model):
    table = []
    for l in model.layers:
        # print("layer %s" % l.layernumber)
        for n in l.neurons:
            for w in n.w:
                line = {
                    "layer": l.layernumber,
                    "neuron": w.neuronnumber,
                    "name": w.name,
                    "type": w.type,
                    "data": w.data,
                    "grad": w.grad,
                }
                table.append(line)
            line = {
                "layer": l.layernumber,
                "neuron": n.b.neuronnumber,
                "name": n.b.name,
                "type": n.b.type,
                "data": n.b.data,
                "grad": n.b.grad,
            }
            table.append(line)

    formatstring = "%5s %3s %3s %2s %6s %6s"
    pline = formatstring % ("name", "lay", "neu", "ty", "data", "grad")
    print(pline)

    for line in table:
        # print(line)
        pline = "%5s %3s %3s %2s %6.2f %6.2f" % (
            line.get("name"),
            line.get("layer"),
            line.get("neuron"),
            line.get("type"),
            line.get("data"),
            line.get("grad"),
        )
        print(pline)


def print_all_values(root):
    nodes, edges = trace(root)
    table = []
    # line={'name','type'}
    for n in nodes:
        # for any value in the graph, add a line
        line = {"name": n.name, "type": n.type, "data": n.data, "grad": n.grad}
        # print(line)
        table.append(line)
    # pp.pprint(table)
    table.sort(key=lambda x: x.get("name"))
    # pp.pprint(table)
    formatstring = "%5s %2s %6s %6s"
    pline = formatstring % ("name", "ty", "data", "grad")
    print(pline)

    for line in table:
        # print(line)
        pline = "%5s %2s %6.2f %6.2f" % (
            line.get("name"),
            line.get("type"),
            line.get("data"),
            line.get("grad"),
        )
        print(pline)


def backupParameters(model):
    originalParams = []
    for l in model.layers:
        # print("layer %s" % l.layernumber)
        for n in l.neurons:
            for w in n.w:
                line = {
                    "layer": l.layernumber,
                    "neuron": w.neuronnumber,
                    "name": w.name,
                    "type": w.type,
                    "data": w.data,
                    "grad": w.grad,
                }
                originalParams.append(line)
            line = {
                "layer": l.layernumber,
                "neuron": n.b.neuronnumber,
                "name": n.b.name,
                "type": n.b.type,
                "data": n.b.data,
                "grad": n.b.grad,
            }
            originalParams.append(line)
    return originalParams

def restoreParameters(model, originalParams):
    for l in model.layers:
        # print("layer %s" % l.layernumber)
        for n in l.neurons:
            for w in n.w:
                print(w.name, w.data)
                # a=originalParams.get('name'=='v001')
                # a='v001' in originalParams
                # print(a)
                for line in originalParams:
                    print(line)
                    a=w.name in line.get('name')
                    print(a)





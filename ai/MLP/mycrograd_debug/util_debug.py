from mycrograd_debug.drawviz_debug import trace

debug_values = False


def debugPrint(model, debugOptions, message="", inputs=[], targets=[], activation={}):
    # print(debugOptions)
    if debugOptions:
        if message:
            print(message)
    if "params" in debugOptions:
        print("parameters")
        print_my_params(model)
    if "allValues" in debugOptions:
        print("allValues")
        print_all_values(activation)
    if inputs:
        print("inputs")
        print(inputs)
    if targets:
        print("targets")
        print(targets)

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
    debug = False
    for l in model.layers:
        # print("layer %s" % l.layernumber)
        for n in l.neurons:
            for w in n.w:
                if debug:
                    print("current_", w.name, w.data)
                # a=originalParams.get('name'=='v001')
                # a='v001' in originalParams
                # print(a)
                for line in originalParams:
                    # print(line)
                    if w.name in line.get("name"):
                        if debug:
                            print("original", w.name, line.get("data"))
                        w.data = line.get("data")
            if debug:
                print("current_", n.b.name, n.b.data)
            for line in originalParams:
                # print(line)
                if n.b.name in line.get("name"):
                    if debug:
                        print("original", n.b.name, line.get("data"))
                    n.b.data = line.get("data")

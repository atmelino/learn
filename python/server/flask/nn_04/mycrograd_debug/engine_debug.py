class Value:
    """stores a single scalar value and its gradient"""

    value_counter = 0
    counter_print = False
    debug_bw = False
    # types
    # w = weight
    # b = additive parameter
    # a = activation
    # i = input

    def __init__(
        self,
        data,
        _children=(),
        _op="",
        name="v",
        layernumber="",
        neuronnumber="",
        weightnumber="",
        type="",
    ):
        Value.value_counter += 1
        self.name = name + str(Value.value_counter).zfill(3)
        self.layernumber = layernumber
        self.neuronnumber = neuronnumber
        self.weightnumber = weightnumber
        self.type = type
        self.data = data
        self.grad = 0

        # print("Value created",self.name)
        # internal variables used for autograd graph construction
        self._backward = lambda: None
        self._prev = set(_children)
        self._op = _op  # the op that produced this node, for graphviz / debugging / etc

    def __add__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data + other.data, (self, other), "+")

        def _backward():
            self_before = self.grad
            other_before = other.grad
            self.grad += out.grad
            other.grad += out.grad
            # print("backward add")
            if self.debug_bw:
                line = (
                    "backward add %s %2s %2s %2s % 6.2f -> % 6.2f  %s %2s %2s %2s % 6.2f -> % 6.2f"
                    % (
                        self.name,
                        self.layernumber,
                        self.neuronnumber,
                        self.type,
                        self_before,
                        self.grad,
                        other.name,
                        other.layernumber,
                        other.neuronnumber,
                        other.type,
                        other_before,
                        other.grad,
                    )
                )
                print(line)
                # print(
                #     "backward add",
                #     self.name,
                #     self.type,
                #     "% 6.2f" % self_before,
                #     "->",
                #     "% 6.2f" % self.grad,
                #     other.name,
                #     "% 6.2f" % other_before,
                #     "->",
                #     "% 6.2f" % other.grad,
                # )

        out._backward = _backward

        return out

    def __mul__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data * other.data, (self, other), "*")

        def _backward():
            self_before = self.grad
            other_before = other.grad
            self.grad += other.data * out.grad
            other.grad += self.data * out.grad
            if self.debug_bw:
                line = (
                    "backward mul %s %2s %2s %2s % 6.2f -> % 6.2f  %s %2s %2s %2s % 6.2f -> % 6.2f"
                    % (
                        self.name,
                        self.layernumber,
                        self.neuronnumber,
                        self.type,
                        self_before,
                        self.grad,
                        other.name,
                        other.layernumber,
                        other.neuronnumber,
                        other.type,
                        other_before,
                        other.grad,
                    )
                )
                print(line)

            #     print(
            #         "backward mul  ",
            #         self.name,
            #         "% 6.2f" % self_before,
            #         "->",
            #         "% 6.2f" % self.grad,
            #         other.name,
            #         "% 6.2f" % other_before,
            #         "->",
            #         "% 6.2f" % other.grad,
            #     )

        out._backward = _backward

        return out

    def __pow__(self, other):
        assert isinstance(
            other, (int, float)
        ), "only supporting int/float powers for now"
        out = Value(self.data**other, (self,), f"**{other}")

        def _backward():
            self.grad += (other * self.data ** (other - 1)) * out.grad

        out._backward = _backward

        return out

    def relu(self):
        out = Value(0 if self.data < 0 else self.data, (self,), "ReLU")

        def _backward():
            self.grad += (out.data > 0) * out.grad

        out._backward = _backward

        return out

    def backward(self):
        # topological order all of the children in the graph
        topo = []
        visited = set()

        def build_topo(v):
            if v not in visited:
                visited.add(v)
                for child in v._prev:
                    build_topo(child)
                topo.append(v)

        build_topo(self)

        # go one variable at a time and apply the chain rule to get its gradient
        self.grad = 1
        for v in reversed(topo):
            v._backward()

    def __neg__(self):  # -self
        return self * -1

    def __radd__(self, other):  # other + self
        return self + other

    def __sub__(self, other):  # self - other
        return self + (-other)

    def __rsub__(self, other):  # other - self
        return other + (-self)

    def __rmul__(self, other):  # other * self
        return self * other

    def __truediv__(self, other):  # self / other
        return self * other**-1

    def __rtruediv__(self, other):  # other / self
        return other * self**-1

    def __repr__(self):
        return f"Value(name={self.name},layernumber={self.layernumber},neuronnumber={self.neuronnumber},weightnumber={self.weightnumber},type={self.type},data={self.data}, grad={self.grad})"

    def reset_counter(self):
        Value.value_counter = 0
        return

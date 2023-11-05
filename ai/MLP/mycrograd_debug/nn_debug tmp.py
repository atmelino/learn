import random
from mycrograd_debug.engine_debug import Value

class Module:

    def zero_grad(self):
        for p in self.parameters():
            p.grad = 0

    def parameters(self):
        return []

class Neuron(Module):

    def __init__(self, nin, layernumber="L", neuronnumber="n", nonlin=True):
        self.neuronnumber = neuronnumber
        self.layernumber = layernumber
        self.w = [
            Value(
                random.uniform(-1, 1),
                type="w"+str(i+1),
                layernumber=self.layernumber,
                neuronnumber=self.neuronnumber,
            )
            for i in range(nin)
        ]
        self.b = Value(
            0, type="b", layernumber=self.layernumber, neuronnumber=self.neuronnumber
        )
        self.nonlin = nonlin
        # print("neuron nonlin is ", self.nonlin)

    def __call__(self, x):
        act = sum((wi * xi for wi, xi in zip(self.w, x)), self.b)
        act.type = "a"
        act.neuronnumber = self.neuronnumber
        act.layernumber = self.layernumber
        return act.relu() if self.nonlin else act

    def parameters(self):
        return self.w + [self.b]

    def __repr__(self):
        return f"{'ReLU' if self.nonlin else 'Linear'}Neuron({len(self.w)})"


class Layer(Module):
    # def __init__(self, nin, nout, nonlin=False, layernumber="L"):
    #     self.neurons = [
    #         Neuron(nin, layernumber, neuronnumber="n" + str(i + 1)) for i in range(nout)
    #     ]

    def __init__(self, nin, nout, **kwargs):
        self.neurons = [Neuron(nin, **kwargs) for _ in range(nout)]

    def __call__(self, x):
        out = [n(x) for n in self.neurons]
        return out[0] if len(out) == 1 else out

    def parameters(self):
        return [p for n in self.neurons for p in n.parameters()]

    def __repr__(self):
        return f"Layer of [{', '.join(str(n) for n in self.neurons)}]"


class MLP(Module):
    def __init__(self, nin, nouts):
        sz = [nin] + nouts
        self.layers = [
            Layer(
                sz[i],
                sz[i + 1],
                layernumber="L" + str(i + 1),
                nonlin=i != len(nouts) - 1,
            )
            for i in range(len(nouts))
        ]

    def __call__(self, x):
        for layer in self.layers:
            x = layer(x)
        return x

    def parameters(self):
        return [p for layer in self.layers for p in layer.parameters()]

    def __repr__(self):
        return f"MLP of [{', '.join(str(layer) for layer in self.layers)}]"


class MLP(Module):
    def __init__(self, nin, nouts):
        sz = [nin] + nouts
        self.layers = [
            Layer(sz[i], sz[i + 1], nonlin=i != len(nouts) - 1)
            for i in range(len(nouts))
        ]

    def __call__(self, x):
        for layer in self.layers:
            x = layer(x)
        return x

    def parameters(self):
        return [p for layer in self.layers for p in layer.parameters()]

    def __repr__(self):
        return f"MLP of [{', '.join(str(layer) for layer in self.layers)}]"


class MLP_linear(Module):
    def __init__(self, nin, nouts):
        sz = [nin] + nouts
        self.layers = [
            Layer(sz[i], sz[i + 1], layernumber="L" + str(i + 1), nonlin=False)
            for i in range(len(nouts))
        ]

    def __call__(self, x):
        for layer in self.layers:
            x = layer(x)
        return x

    def parameters(self):
        return [p for layer in self.layers for p in layer.parameters()]

    def __repr__(self):
        return f"MLP of [{', '.join(str(layer) for layer in self.layers)}]"

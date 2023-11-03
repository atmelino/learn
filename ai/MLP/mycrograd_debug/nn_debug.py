import random
from mycrograd_debug.engine_debug import Value


class Module:
    def zero_grad(self):
        for p in self.parameters():
            p.grad = 0

    def parameters(self):
        return []

    layer_counter = 0


class Neuron(Module):
    neuron_counter = 0
    nnum="n0"

    # def __init__(self, nin, nonlin=True):
    def __init__(self, nin, layer_counter=0, nonlin=False):
        Neuron.neuron_counter += 1
        Neuron.nnum = "n" + str(Neuron.neuron_counter)
        lnum = "l" + str(Layer.layer_counter)

        self.w = [
            Value(random.uniform(-1, 1), type="w", layernumber=lnum, neuronnumber=Neuron.nnum)
            for _ in range(nin)
        ]
        self.b = Value(0, type="b", layernumber=lnum, neuronnumber=Neuron.nnum)
        self.nonlin = nonlin
        # print("neuron nonlin is ", self.nonlin)

    def __call__(self, x):
        act = sum((wi * xi for wi, xi in zip(self.w, x)), self.b)
        act.type = "a"
        act.neuronnumber=x.nnum
        return act.relu() if self.nonlin else act

    def parameters(self):
        return self.w + [self.b]

    def __repr__(self):
        return f"{'ReLU' if self.nonlin else 'Linear'}Neuron({len(self.w)})"


class Layer(Module):
    def __init__(self, nin, nout, **kwargs):
        Layer.layer_counter += 1

        # print("Layer kwargs",**kwargs)
        self.neurons = [Neuron(nin, Layer.layer_counter, **kwargs) for _ in range(nout)]

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
        self.layers = [Layer(sz[i], sz[i + 1], nonlin=False) for i in range(len(nouts))]

    def __call__(self, x):
        for layer in self.layers:
            x = layer(x)
        return x

    def parameters(self):
        return [p for layer in self.layers for p in layer.parameters()]

    def __repr__(self):
        return f"MLP of [{', '.join(str(layer) for layer in self.layers)}]"

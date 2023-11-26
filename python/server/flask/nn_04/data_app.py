import random
import numpy as np
import pprint

from mycrograd_debug.engine_debug import Value
from mycrograd_debug.nn_debug import Neuron, Layer, MLP
from mycrograd_debug.drawviz_debug import draw_dot, draw_nn, print_my_params

np.random.seed(1337)
random.seed(1337)
pp = pprint.PrettyPrinter(indent=4)

from flask import Flask, request, jsonify, after_this_request
from graphviz import Digraph
import datetime

app = Flask(__name__)
global counter
global flipflop
counter = 1
flipflop = True

# initialize a model
nin = 1  # number of inputs
nout = 1  # number of outputs
Value.value_counter = 0
model = MLP(
    nin, [2, nout], lastReLU=False, weightsinit=2, debug_bw=True
)  # 2-layer neural network
xinumbers = list(range(4, 4 + nin))
xinput = [Value(x, type="i%s" % index) for index, x in enumerate(xinumbers, start=1)]
global activation


# activation = model(xinput)


def act():
    global activation
    #### forward pass0
    activation = model(xinput)


def zeroGrad():
    global activation
    model.zero_grad()
    print("zero'd gradients")
    pp.pprint(model.parameters())


def back():
    #### backward pass
    global activation
    activation.backward()
    print("parameters after backpass")
    pp.pprint(model.parameters())


def upd():
    #### update
    global activation
    for p in model.parameters():
        p.data += -0.1 * p.grad
    print("updated parameters")
    pp.pprint(model.parameters())


def getactivation(filename="default"):
    global activation
    global counter
    counter = counter + 1
    act()
    # dot=draw_nn(xinput, model)
    dot = draw_nn(xinput, model, debug_print_01=True)
    dot.node(name="a", label="hello %3d" % counter, shape="record")
    dot.render("static/" + filename)


def backward(filename="default"):
    global activation
    global counter
    counter = counter + 1
    back()
    dot = draw_nn(xinput, model)
    dot.node(name="a", label="hello %3d" % counter, shape="record")
    dot.render("static/" + filename)


def zeroGradients(filename="default"):
    global counter
    counter = counter + 1
    zeroGrad()
    dot = draw_nn(xinput, model)
    dot.node(name="a", label="hello %3d" % counter, shape="record")
    dot.render("static/" + filename)

def updateParams(filename="default"):
    upd()



@app.route("/", methods=["POST", "GET"])
def hello():
    global flipflop
    print("counter=%3d" % counter)
    flipflop = not flipflop

    print("hello called")
    print(request)
    print(request.data)
    cmd = request.args.get("cmd")
    print(cmd)

    filename = "img1" if flipflop else "img2"

    # filename="static/hello%3d" % counter
    # filename = "hello" + str(counter).zfill(3)

    print(filename)

    @after_this_request
    def add_header(response):
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response

    if cmd == "act":
        getactivation(filename)
        jsonResp = {"image": filename + ".svg", "sape": 4139}
    if cmd == "bwd":
        backward(filename)
        jsonResp = {"image": filename + ".svg", "sape": 4139}
    if cmd == "zer":
        zeroGradients(filename)
        jsonResp = {"image": filename + ".svg", "sape": 4139}
    print(jsonResp)
    return jsonify(jsonResp)


if __name__ == "__main__":
    app.run(host="localhost", port=8989)

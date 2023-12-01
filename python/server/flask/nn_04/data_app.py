import random
import numpy as np
import pprint

from mycrograd_debug.engine_debug import Value
from mycrograd_debug.nn_debug import Neuron, Layer, MLP
from mycrograd_debug.drawviz_debug import (
    draw_dot,
    draw_nn,
    print_all_values,
    print_my_params,
    backupParameters,
    restoreParameters,
)

np.random.seed(1337)
random.seed(1337)
pp = pprint.PrettyPrinter(indent=4)

from flask import Flask, request, jsonify, after_this_request
from graphviz import Digraph
import datetime

app = Flask(__name__)
global model
global counter
global flipflop
global activation
debug_parameters = True
debug_values = False
counter = 1
flipflop = True

# initialize a model
nin = 1  # number of inputs
nout = 1  # number of outputs
Value.value_counter = 0
model = MLP(nin, [2, nout], lastReLU=False, weightsinit=2, debug_bw=True)
originalParams = backupParameters(model)

xinumbers = list(range(4, 4 + nin))
xinput = [Value(x, type="i%s" % index) for index, x in enumerate(xinumbers, start=1)]


def act():
    #### forward pass0
    global model
    global activation
    activation = model(xinput)
    if debug_parameters:
        print_my_params(model)
    if debug_values:
        print_all_values(activation)


def zeroGrad():
    global model
    model.zero_grad()
    for i in xinput:
        i.grad = 0
    print("zero'd gradients")
    if debug_parameters:
        print_my_params(model)
    if debug_values:
        print_all_values(activation)


def back():
    #### backward pass
    global activation
    activation.backward()
    print("parameters after backpass")
    if debug_parameters:
        print_my_params(model)
    if debug_values:
        print_all_values(activation)


def upd():
    #### update
    global model
    for p in model.parameters():
        p.data += -0.1 * p.grad
    print("updated parameters")
    if debug_parameters:
        print_my_params(model)
    if debug_values:
        print_all_values(activation)


def getactivation(filename="default"):
    global model
    global activation
    global counter
    counter = counter + 1
    act()
    loss=activation*activation
    # dot=draw_nn(xinput, model)
    dot = draw_nn(xinput, model, debug_print_01=True)
    dot.node(name="a", label="clicked %3d" % counter, shape="record")
    dot.node(name="b", label="loss %6.2f" % loss.data, shape="record")
    dot.render("static/" + filename)

def zeroGradients(filename="default"):
    global model
    global counter
    counter = counter + 1
    zeroGrad()
    dot = draw_nn(xinput, model)
    dot.node(name="a", label="clicked %3d" % counter, shape="record")
    dot.render("static/" + filename)

def backward(filename="default"):
    global model
    global activation
    global counter
    counter = counter + 1
    back()
    dot = draw_nn(xinput, model)
    dot.node(name="a", label="clicked %3d" % counter, shape="record")
    dot.render("static/" + filename)

def updateParams(filename="default"):
    global model
    global counter
    counter = counter + 1
    upd()
    dot = draw_nn(xinput, model)
    dot.node(name="a", label="clicked %3d" % counter, shape="record")
    dot.render("static/" + filename)

def optStep(filename="default"):
    global model
    global counter
    counter = counter + 1
    act()
    zeroGrad()
    back()
    upd()
    dot = draw_nn(xinput, model)
    dot.node(name="a", label="clicked %3d" % counter, shape="record")
    dot.render("static/" + filename)


def resetModel(filename="default"):
    global model
    global activation
    global counter
    counter = counter + 1
    restoreParameters(model, originalParams)
    print("restored model params")
    print_my_params(model)
    dot = draw_nn(xinput, model)
    dot.node(name="a", label="clicked %3d" % counter, shape="record")
    dot.render("static/" + filename)


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
    if cmd == "upd":
        updateParams(filename)
        jsonResp = {"image": filename + ".svg", "sape": 4139}
    if cmd == "ost":
        optStep(filename)
        jsonResp = {"image": filename + ".svg", "sape": 4139}
    if cmd == "res":
        resetModel(filename)
        jsonResp = {"image": filename + ".svg", "sape": 4139}
    print(jsonResp)
    return jsonify(jsonResp)


if __name__ == "__main__":
    app.run(host="localhost", port=8989)

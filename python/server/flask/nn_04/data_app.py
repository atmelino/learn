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
from mycrograd_debug.util_debug import debugFunc

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
global loss
debug_parameters = True
debug_values = False
counter = 1
flipflop = True

# initialize a model
nin = 1  # number of inputs
nout = 1  # number of outputs
Value.value_counter = 0
model = MLP(nin, [2, nout], lastReLU=False, weightsinit=2, debug_bw=False)
xinumbers = list(range(4, 4 + nin))
xinput = [Value(x, type="i%s" % index) for index, x in enumerate(xinumbers, start=1)]
xtarget = Value(1.2, type="t")  # desired targets
debugFunc(
    model,
    {"parameters"},
    message="start",
    inputs=xinput,
    targets=xtarget,
)

originalParams = backupParameters(model)

def imageFunc(filename="default"):
    # dot=draw_nn(xinput, model)
    dot = draw_nn(xinput, model, debug_print_01=True)
    # dot.node(name="a", label="clicked %3d" % counter, shape="record")
    dot.node(name="lossLabel", label="loss %6.2f" % loss.data, shape="record")
    dot.render("static/" + filename)


# loss function single MLP
def loss_single(activation, target):
    total_loss = (activation - target)*(activation - target)
    total_loss.type="l"
    return total_loss

def act(filename="default"):
    #### forward pass0
    global model
    global loss
    global activation
    global counter
    counter = counter + 1
    activation = model(xinput)
    loss = loss_single(activation, xtarget)
    debugFunc(model, {"parameters"}, message="act")
    imageFunc(filename)


def zeroGrad(filename="default"):
    global model
    global counter
    counter = counter + 1
    model.zero_grad()
    for i in xinput:
        i.grad = 0
    # print("zero'd gradients")
    debugFunc(model, {"parameters"}, message="zer")
    imageFunc(filename)


def back(filename="default"):
    #### backward pass
    global activation
    global counter
    counter = counter + 1
    activation.backward()
    # print("parameters after backpass")
    debugFunc(model, {"parameters"}, message="bwd")
    imageFunc(filename)


def upd(filename="default"):
    #### update
    global model
    global counter
    counter = counter + 1
    for p in model.parameters():
        p.data += -0.05 * p.grad
    # print("updated parameters")
    debugFunc(model, {"parameters"}, message="upd")
    imageFunc(filename)


def getactivation(filename="default"):
    global model
    global activation
    act()


def zeroGradients(filename="default"):
    global model
    zeroGrad()


def backward(filename="default"):
    global model
    global activation
    back()
    imageFunc(filename)


def updateParams(filename="default"):
    global model
    global loss
    upd()


def optStep(filename="default"):
    global model
    global loss
    global counter
    counter = counter + 1
    act()
    zeroGrad()
    back()
    upd()
    print(f"step %3d output %6.4f loss %6.4f" % (counter, activation.data, loss.data))
    imageFunc(filename)


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

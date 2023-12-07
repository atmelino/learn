import random
import numpy as np
import pprint

from mycrograd_debug.engine_debug import Value
from mycrograd_debug.nn_debug import Neuron, Layer, MLP
from mycrograd_debug.drawviz_debug import draw_dot, draw_nn
from mycrograd_debug.util_debug import (
    debugPrint,
    print_my_params,
    print_all_values,
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
global step
global flipflop
global activation
global loss
step = 0
flipflop = True
# debugOptions={"params"}
debugOptions = {}

# initialize a model
nin = 1  # number of inputs
nout = 1  # number of outputs
Value.value_counter = 0
model = MLP(nin, [2, nout], lastReLU=False, weightsinit=2, debug_bw=False)
# xinumbers = list(range(1, 1 + nin))
xinumbers = [4]
xinput = [Value(x, type="i%s" % index) for index, x in enumerate(xinumbers, start=1)]
xtarget = Value(3, type="t")  # desired targets
# xtarget = Value(0.0, type="t")  # desired targets
debugPrint(model, {"params"}, message="start", inputs=xinput, targets=xtarget)
originalParams = backupParameters(model)


def imageFunc(filename="default"):
    # dot=draw_nn(xinput, model)
    dot = draw_nn(xinput, model, debug_print_01=False)
    # dot.node(name="a", label="clicked %3d" % counter, shape="record")
    dot.node(
        name="loss", label="step %2d loss %6.2f" % (step, loss.data), shape="record"
    )
    dot.render("static/" + filename)


# loss function single MLP
def loss_single(activation, target):
    total_loss = (activation - target) * (activation - target)
    # total_loss = activation*activation
    total_loss.type = "l"
    return total_loss


def getactivation(filename="default"):
    #### forward pass0
    global model
    global loss
    global activation
    global step
    step = step + 1
    activation = model(xinput)
    loss = loss_single(activation, xtarget)
    debugPrint(model, debugOptions, message="act")
    imageFunc(filename)


def zeroGradients(filename="default"):
    global model
    global step
    model.zero_grad()
    for i in xinput:
        i.grad = 0
    # print("zero'd gradients")
    debugPrint(model, debugOptions, message="zer")
    imageFunc(filename)


def backward(filename="default"):
    #### backward pass
    global activation
    global step
    loss.backward()
    # print("parameters after backpass")
    debugPrint(model, debugOptions, message="bwd")
    imageFunc(filename)


def updateParams(filename="default"):
    #### update
    global model
    global step
    for p in model.parameters():
        p.data += -0.05 * p.grad
    # print("updated parameters")
    debugPrint(model, debugOptions, message="upd")
    imageFunc(filename)


def optStep(filename="default"):
    global model
    global loss
    global step
    getactivation()
    zeroGradients()
    backward()
    updateParams()
    print(f"step %3d output %6.4f loss %6.4f" % (step, activation.data, loss.data))
    imageFunc(filename)


def resetModel(filename="default"):
    global model
    global loss
    global step
    restoreParameters(model, originalParams)
    zeroGradients()
    getactivation()
    step = 0
    print("restored model params")
    dot = draw_nn(xinput, model, debug_print_01=True)
    dot.render("static/" + filename)


@app.route("/", methods=["POST", "GET"])
def hello():
    global flipflop
    print("step=%3d" % step)
    flipflop = not flipflop

    # print("hello called")
    # print(request)
    # print(request.data)
    cmd = request.args.get("cmd")
    # print(cmd)

    filename = "img1" if flipflop else "img2"
    # print(filename)

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
    # print(jsonResp)
    return jsonify(jsonResp)


if __name__ == "__main__":
    app.run(host="localhost", port=8989)

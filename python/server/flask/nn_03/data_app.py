from flask import Flask, request, jsonify, after_this_request
from graphviz import Digraph
import datetime

app = Flask(__name__)
global counter
counter=1

def generateSVG(filename="default"):
    # now = datetime.datetime.now()
    dot = Digraph(format="svg", graph_attr={"rankdir": "LR"})  # LR = left to right
    nodes, edges = set(), set()
    # dot.node(name="a", label="hello %s" % now, shape="record")
    dot.node(name="a", label="hello %3d" % counter, shape="record")
    dot.render("static/"+filename)


@app.route("/", methods=["POST", "GET"])
def hello():
    print("hello called")
    print(request)
    print(request.data)
    cmd = request.args.get("cmd")
    print(cmd)

    global counter
    counter=counter+1
    print("counter=%3d" % counter)
    # filename="static/hello%3d" % counter
    filename = "hello" + str(counter).zfill(3)

    print(filename)

    # generateSVG("static/hello2")
    generateSVG(filename)

    @after_this_request
    def add_header(response):
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response

    if cmd == "act":
        jsonResp = {"image": "nn_02.svg", "sape": 4139}
    if cmd == "bwd":
        jsonResp = {"image": filename+".svg", "sape": 4139}
    print(jsonResp)
    return jsonify(jsonResp)


if __name__ == "__main__":
    app.run(host="localhost", port=8989)

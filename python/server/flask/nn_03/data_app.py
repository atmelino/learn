from flask import Flask, request, jsonify, after_this_request
from graphviz import Digraph
import datetime

app = Flask(__name__)
global counter
global flipflop
counter=1
flipflop=True

def generateSVG(filename="default"):
    global counter
    counter=counter+1

    # now = datetime.datetime.now()
    dot = Digraph(format="svg", graph_attr={"rankdir": "LR"})  # LR = left to right
    nodes, edges = set(), set()
    # dot.node(name="a", label="hello %s" % now, shape="record")
    dot.node(name="a", label="hello %3d" % counter, shape="record")
    dot.render("static/"+filename)


@app.route("/", methods=["POST", "GET"])
def hello():
    global flipflop
    print("counter=%3d" % counter)
    flipflop=not flipflop

    print("hello called")
    print(request)
    print(request.data)
    cmd = request.args.get("cmd")
    print(cmd)

    filename="img1" if flipflop else "img2"


    # filename="static/hello%3d" % counter
    # filename = "hello" + str(counter).zfill(3)

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

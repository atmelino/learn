from flask import Flask, request, jsonify, after_this_request
from graphviz import Digraph
import datetime

app = Flask(__name__)
dot = Digraph(format="svg", graph_attr={"rankdir": "LR"})  # LR = left to right
nodes, edges = set(), set()
counter=1

def generateSVG(name="default"):
    now = datetime.datetime.now()

    # self.counter+=1
    dot.node(name="a", label="hello %s" % now, shape="record")
    dot.render(name)


@app.route("/", methods=["POST", "GET"])
def hello():
    print("hello called")
    print(request)
    print(request.data)
    cmd = request.args.get("cmd")
    print(cmd)

    generateSVG("static/hello2")

    @after_this_request
    def add_header(response):
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response

    if cmd == "act":
        jsonResp = {"image": "nn_02.svg", "sape": 4139}
    if cmd == "bwd":
        jsonResp = {"image": "hello2.svg", "sape": 4139}
    print(jsonResp)
    return jsonify(jsonResp)


if __name__ == "__main__":
    app.run(host="localhost", port=8989)

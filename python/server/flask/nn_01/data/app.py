from flask import Flask, request, jsonify, after_this_request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def hello():
    print("hello called")
    print(request)
    print(request.data)
    cmd = request.args.get('cmd')
    print(cmd)
    @after_this_request
    def add_header(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    if cmd=='act':
        jsonResp = {'image': 'nn_02.svg', 'sape': 4139}
    if cmd=='bwd':
        jsonResp = {'image': 'nn_03.svg', 'sape': 4139}
    print(jsonResp)
    return jsonify(jsonResp)


if __name__ == '__main__':
    app.run(host='localhost', port=8989)




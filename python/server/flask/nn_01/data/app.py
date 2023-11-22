from flask import Flask, request, jsonify, after_this_request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    @after_this_request
    def add_header(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    jsonResp = {'image': 'hello.svg', 'sape': 4139}
    print(jsonResp)
    return jsonify(jsonResp)

if __name__ == '__main__':
    app.run(host='localhost', port=8989)

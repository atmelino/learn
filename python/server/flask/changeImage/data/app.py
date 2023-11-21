from flask import Flask, request, jsonify, after_this_request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    @after_this_request
    def add_header(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

    jsonResp = {'jack': 4098, 'sape': 4139}
    print(jsonResp)
    return jsonify(jsonResp)

if __name__ == '__main__':
    app.run(host='localhost', port=8989)













# http://localhost:8989/hello
# http://127.0.0.1:8989


# http://127.0.0.1:5000/hello

# from flask import Flask, request, jsonify, after_this_request, render_template

# app = Flask(__name__)


# @app.route("/", methods=["GET"])
# def hello():
#     print(request)
#     @after_this_request
#     def add_header(response):
#         response.headers.add('Access-Control-Allow-Origin', '*')
#         return response
#     jsonResp = {'jack': 4098, 'sape': 4139}
#     print(jsonResp)
#     return jsonify(jsonResp)

    
#     if request.method == 'POST':
#            print("POST request")

#     if request.method == 'GET':
#            print("GET request")







#     @after_this_request
#     def add_header(response):
#         response.headers.add("Access-Control-Allow-Origin", "*")
#         return response

#     jsonResp = {"jack": 4098, "sape": 4139}
#     print(jsonResp)
#     return jsonify(jsonResp)


# if __name__ == "__main__":
#     # app.run(host='localhost', port=8989)
#     # app.run(port=8989)
#    app.run(debug = True)

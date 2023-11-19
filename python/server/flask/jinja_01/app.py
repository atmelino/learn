#!/usr/bin/python

# start with flask run

# then go to http://127.0.0.1:5000/greet?name=Peter


from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/greet")
def greet():
    username = request.args.get('name')
    return render_template('index.html', name=username)

if __name__ == "__main__":
    app.run()
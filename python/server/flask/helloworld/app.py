# save this as app.py

# to run:
# change into this folder
# and run
# flask run

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"
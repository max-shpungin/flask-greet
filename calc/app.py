# Put your app in here.
from flask import Flask, request
import operations

app = Flask(__name__)

@app.get("/add")
def add_endpoint():
    return str(operations.add(int(request.args["a"]), int(request.args["b"])))

@app.get("/sub")
def sub_endpoint():
    return str(operations.sub(int(request.args["a"]), int(request.args["b"])))

@app.get("/mult")
def mult_endpoint():
    return str(operations.mult(int(request.args["a"]), int(request.args["b"])))

@app.get("/div")
def div_endpoint():
    return str(operations.div(int(request.args["a"]), int(request.args["b"])))
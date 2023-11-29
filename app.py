from flask import Flask, request

"""routes for /welcome"""

app = Flask(__name__)

@app.get("/welcome")
def welcome_page():
    return "welcome"

@app.get("/welcome/home")
def welcome_home_page():
    return "welcome home"

@app.get("/welcome/back")
def welcome_back_page():
    return "welcome back"




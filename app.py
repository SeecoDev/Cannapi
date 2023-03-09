from flask import Flask, jsonify
import json

app = Flask(__name__)



@app.route("/")
def main():
    return "<center><h1>HOLA ITE</h1></center><marquee>ADRIAN CHAD</marquee>"

@app.route("/about")
def about():
    with open('cannapi.json',"r") as json:
        display = json.read()   
        return display


@app.route("/bye")
def adios():
    return "<h1> Recuerden fumar bandita</h1>"


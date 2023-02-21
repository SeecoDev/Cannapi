from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return "HOLA ITE"

@app.route("/bye")
def adios():
    return "Hasta luego putitos"

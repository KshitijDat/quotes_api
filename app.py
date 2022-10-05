from flask import Flask
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
    return "<h3>Welcome to Quotes API! Go to /getquote to get a random quote in form of json</h3>"

@app.route("/getquote")
def fetchquote():
    return "this is a quote!"

if __name__ == '__main__':
    app.run()
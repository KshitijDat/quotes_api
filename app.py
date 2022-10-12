from urllib import request
from flask import Flask
import pandas as pd
from requests import get
from json import loads

app = Flask(__name__)

@app.route("/")
def index():
    return "<h3>Welcome to Quotes API! Go to /getquote to get a random quote in form of json</h3>"

@app.route("/getquote")
def fetchquote():
    response = get("https://zenquotes.io/api/random")
    response = loads(response)
    response = {"quote":response[0]['q'],"author":response[0]['a']}
    return response

if __name__ == '__main__':
    app.run()
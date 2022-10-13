from flask import Flask, render_template
import pandas as pd
from requests import get

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('quotes.html')

@app.route("/getquote")
def fetchquote():
    response = get("https://zenquotes.io/api/random")
    response = response.json()
    response = {"quote":response[0]['q'],"author":response[0]['a']}
    return response

if __name__ == '__main__':
    app.run()
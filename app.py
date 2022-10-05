from flask import Flask
from requests import get
from json import loads

app = Flask(__name__)

#Fetch Quotes from zenquotes.io 
def get_quote():
    response = get("https://zenquotes.io/api/random")
    json_data = loads(response.text)
    quotes = json_data[0]['q'] + "-" + json_data[0]['a']
    return (quotes)

@app.route("/")
def index():
    return "<h3>Welcome to Quotes API! Go to <a href='/getquote'>/getquote</a> to get a random quote in form of json</h3>"

@app.route("/getquote")
def fetchquote():
    return get_quote()

if __name__ == '__main__':
    app.run(debug=True,port=8000)
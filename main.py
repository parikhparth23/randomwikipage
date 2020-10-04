from flask import Flask
import requests

app = Flask(__name__)


@app.route('/')
def home():
    baseurl = "https://en.wikipedia.org/wiki/Special:Random"
    result = requests.get(baseurl)
    return result.content


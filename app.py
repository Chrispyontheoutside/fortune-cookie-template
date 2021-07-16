from flask import Flask, render_template
import requests
import json 

app = Flask(__name__)


@app.route("/")
def fortune_cookie():
    ## Get the request from the website
    ## Get the json
    ## Get the advice from inside the slip
    #Give our HTML file the slip
if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 8080)

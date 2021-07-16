from flask import Flask, render_template
import requests
import json 

app = Flask(__name__)


@app.route("/")
def fortune_cookie():
    ## Get the request from the website
    response = requests.get("https://api.adviceslip.com/advice")
    ## Get the json
    advice = response.json()
    ## Get the advice from inside the slip
    advice = advice["slip"]["advice"]
    #Give our HTML file the slip
    return render_template('index.html',advice = advice)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 8080)
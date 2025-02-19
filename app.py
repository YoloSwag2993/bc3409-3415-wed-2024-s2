from flask import Flask
from flask import render_template,request
import textblob

app = Flask(__name__)

@app.route("/", methods=["Get","POST"])
def index():
    return(render_template("index.html"))

@app.route("/prediction", methods=["Get","POST"])
def prediction():
    return(render_template("prediction.html"))

@app.route("/predicted_DBS", methods=["Get","POST"])
def predicted_DBS():
    q = float(request.form.get("q"))
    return(render_template("predicted_DBS.html",r=(-50.6*q)+90.2))

@app.route("/text_sentiment", methods=["Get","POST"])
def text_sentiment():
    return(render_template("text_sentiment.html"))

@app.route("/sentiment_result", methods=["Get","POST"])
def sentiment_result():
    q = (request.form.get("q"))
    r = textblob.TextBlob(q).sentiment
    return(render_template("sentiment_result.html",r=r))

if __name__ == "__main__":
    app.run()
from flask import Flask
from flask import render_template,request

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

if __name__ == "__main__":
    app.run()
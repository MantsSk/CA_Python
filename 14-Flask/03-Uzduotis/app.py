from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", date = datetime.now())

@app.route("/name")
def name():
    return render_template("names.html", name = "Tomas")

@app.route("/<word>")
def word(word):
    return render_template("words.html", word = word)

if __name__ == "__main__":
    app.run(debug=True)
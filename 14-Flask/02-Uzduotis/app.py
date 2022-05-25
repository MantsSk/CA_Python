from flask import Flask, render_template

app = Flask(__name__)

app.config.update(
    TEMPLATES_AUTO_RELOAD = True
)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
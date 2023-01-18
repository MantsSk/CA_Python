from flask import Flask, jsonify, request
from calendar import isleap

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if (request.method == 'POST'):
        some_json = request.get_json()
        return jsonify({'you sent': some_json})
    else:
        return jsonify({'about': 'Hello World'})


@app.route("/leap/<int:year>", methods=['GET'])
def keliamieji(year):
    if isleap(year):
        return jsonify({'result': "Leap"})
    else:
        return jsonify({'result': "Not leap"})


if __name__ == '__main__':
    app.run(port=8000, debug=True)

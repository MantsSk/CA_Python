from flask import Flask, request
from flask_restful import Resource, Api
from calendar import isleap

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    # Parametras 'self' yra būtinas
    # metodo pavadinimas turi būti norimo requesto pavadinimas: get, post, delete, etc.
    def get(self):
        return {'about': 'Hello world!'}

    # Parametras 'self' yra būtinas
    # metodo pavadinimas turi būti norimo requesto pavadinimas: get, post, delete, etc.
    def post(self):
        body = request.get_json()
        return {'you sent': body}, 200  # Galima nurodyti status kodą


class Leap(Resource):
    # Parametras 'self' yra būtinas
    # metodo pavadinimas turi būti norimo requesto pavadinimas: get, post, delete, etc.
    def get(self, year):
        if isleap(year):
            return {'result': "Leap"}
        else:
            return {'result': "Not leap"}


# užregistruojame endpointą, nurodome route'ą. kaip tą endpointą pasiekti
api.add_resource(HelloWorld, '/')
# užregistruojame endpointą, nurodome route'ą. kaip tą endpointą pasiekti
api.add_resource(Leap, '/leap/<int:year>')

if __name__ == '__main__':
    app.run(port=8000, debug=True)

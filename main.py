from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

names = {
  "Ella": {
    "age": 4,
    "food": "peanut butter"
  },
  "Linus": {
    "age": 6,
    "food": "sweet potato"
  }
}

class HelloElla(Resource):
  def get(self, name):
    return names[name]

  def post(self):
    return {"data": "Ella, can you post up."}

api.add_resource(HelloElla, "/helloella/<string:name>")
 
if __name__ == "__main__":
  app.run(debug=True)
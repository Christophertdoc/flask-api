from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class HelloElla(Resource):
  def get(self):
    return {"Ella can you get me a Hello"}

api.add_resource(HelloElla, "/helloella")
 
if __name__ == "__main__":
  app.run(debug=True)
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api()


class Main(Resource):
    def get(self):
        return {"db": "addrebook", "sd": 56}


api.add_resource(Main, "/api/server")

api.init_app(app)


if __name__ == "__main__":
    app.run(debug=True, port=5000, host="127.0.0.1")

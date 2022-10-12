from flask import Flask, jsonify
from flask_restful import Api, Resource
from server_db import table_users

app = Flask(__name__)
api = Api()


class Main(Resource):
    def get(self):
        return jsonify(table_users)


api.add_resource(Main, "/api/users")

api.init_app(app)


if __name__ == "__main__":
    app.run(debug=True, port=3000, host="127.0.0.1")

from flask_restful import Api, Resource

from src.app import create_app

app = create_app()
api = Api(app)


class Index(Resource):
    def get(self):
        return "Welcome"


class Example(Resource):
    def get(self):
        pass

    def options(self):
        allowed_methods = ["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD"]
        response_headers = {"Allow": ", ".join(allowed_methods)}
        return "", 200, response_headers


api.add_resource(Index, "/")
api.add_resource(Example, "/<string:todo_id>")

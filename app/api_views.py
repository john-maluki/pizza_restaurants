from flask_restful import Resource
from app import rest_api


class RestaurantResourse(Resource):
    def get(self):
        return "api is working"


rest_api.add_resource(RestaurantResourse, "/")

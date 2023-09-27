from app import rest_api
from flask_restx import fields

restaurant_input_api_model = rest_api.model(
    "RestaurantPizza",
    {
        "price": fields.Integer,
        "pizza_id": fields.Integer,
        "restaurant_id": fields.Integer,
    },
)

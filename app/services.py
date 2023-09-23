from app.models import Restaurant, Pizza, RestaurantPizza
from app.exceptions import (
    RestaurantNotFoundException,
)


class RestaurantService:
    @classmethod
    def get_all_restaurants(cls):
        restaurants = Restaurant.query.all()
        return restaurants

    @classmethod
    def get_restaurant_by_id(cls, id):
        restaurant = Restaurant.query.filter_by(id=id).first()
        if restaurant:
            return restaurant
        else:
            raise RestaurantNotFoundException("Restaurant not found")


class PizzaService:
    @classmethod
    def get_all_pizzas(cls):
        pizzas = Pizza.query.all()
        return pizzas

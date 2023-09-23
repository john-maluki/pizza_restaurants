from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()


class Pizza(db.Model, SerializerMixin):
    __tablename__ = "pizzas"

    serialize_rules = ("-restaurant_pizzas.pizza",)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    ingredients = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    restaurant_pizzas = db.relationship("RestaurantPizza", backref="pizza")

    def __repr__(self):
        return f"<Pizza {self.name}>"


class Restaurant(db.Model, SerializerMixin):
    __tablename__ = "restaurants"

    serialize_rules = ("-restaurant_pizzas.restaurant",)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    address = db.Column(db.String)

    restaurant_pizzas = db.relationship("RestaurantPizza", backref="restaurant")

    def __repr__(self):
        return f"<Restaurant {self.name} {self.address}>"


class RestaurantPizza(db.Model, SerializerMixin):
    __tablename__ = "restaurant_pizzas"

    serialize_rules = ("-pizza.restaurant_pizzas",)
    serialize_rules = ("-restaurant.restaurant_pizzas",)

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(
        db.Integer,
        db.CheckConstraint(
            "price >=1 AND price <=30", name="Price value is not with range 1 and 30"
        ),
    )
    pizza_id = db.Column(db.Integer, db.ForeignKey("pizzas.id"))
    restaurant_id = db.Column(db.Integer, db.ForeignKey("restaurants.id"))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f"<RestaurantPizza {self.price}>"

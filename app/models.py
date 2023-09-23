from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Pizza(db.Model):
    __tablename__ = "pizzas"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    ingredients = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    restaurant_pizzas = db.relationship("RestaurantPizza", backref="pizza")

    def __repr__(self):
        return f"<Pizza {self.name}>"


class Restaurant(db.Model):
    __tablename__ = "restaurants"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    address = db.Column(db.String)

    restaurant_pizzas = db.relationship("RestaurantPizza", backref="restaurant")

    def __repr__(self):
        return f"<Restaurant {self.name} {self.address}>"


class RestaurantPizza(db.Model):
    __tablename__ = "restaurant_pizza"

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer)
    pizza_id = db.Column(db.Integer, db.ForeignKey("pizzas.id"))
    restaurant_id = db.Column(db.Integer, db.ForeignKey("restaurants.id"))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # Add CheckConstraint to enforce min and max values for price
    min_price = 1
    max_price = 30

    __table_args__ = (
        db.CheckConstraint(
            f"{price} >= {min_price} AND {price} <= {max}", name="check_value_range"
        ),
    )

    def __repr__(self):
        return f"<RestaurantPizza {self.price} Restaurant:{self.restaurant} Pizza: {self.pizza}>"

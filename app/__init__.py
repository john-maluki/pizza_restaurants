from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from app.models import db

app = Flask(__name__)
app.config["SECRET_KEY"] = "jdbwejbfewub=wehdweh64wdhwvh-bhcb"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///restaurant_pizza.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

rest_api = Api(app)

from app import api_views
from app import models

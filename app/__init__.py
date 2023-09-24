from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from app.models import db

app = Flask(__name__)
app.config.from_pyfile("settings.py")
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

rest_api = Api(app)

from app import api_views
from app import models

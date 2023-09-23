from flask import Flask
from app.extensions import extend_app


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "jdbwejbfewub=wehdweh64wdhwvh-bhcb"
    extend_app(app)
    return app


app = create_app()

from app.views import api_views
from app.db import models

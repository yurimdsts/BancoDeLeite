from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from .config import Config
from os import path

db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    app = Flask(
        __name__,
        template_folder=path.join(path.dirname(path.dirname(path.dirname(__file__))), 'frontend', 'templates'),
        static_folder=path.join(path.dirname(path.dirname(path.dirname(__file__))), 'frontend', 'static')
    )

    app.config.from_object(Config)

    db.init_app(app)
    ma.init_app(app)
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
from flask import Flask
from flask_pymongo import PyMongo
from router.main import main as main_controller

mongo = PyMongo()

def create_app(config_object='app.configs.Development'):
    app = Flask(__name__)
    app.config.from_object(config_object)
    mongo.init_app(app)
    app.register_blueprint(main_controller)

    return app
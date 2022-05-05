from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv # function that loads dotenv
import os 

db = SQLAlchemy() # creating new DB obj - we can import db into other files because outside of method
migrate = Migrate() # creating new migrate obj
load_dotenv()

def create_app(testing = None): 
    # __name__ stores the name of the module we're in
    app = Flask(__name__)

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 
    if testing is None:
        # telling sqlalchemy where our db is located
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('SQLALCHEMY_DATABASE_URI')
    else: 
        app.config['TESTING'] = True 
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('SQLALCHEMY_TESTING_DATABASE_URI') 

    db.init_app(app) # hooking up db and app - connecting objs to flask server
    migrate.init_app(app, db) # hooking up migrate and app - connecting objs to flask server

    from .models.cars import Car # db and migration able to know that it exists 

    from .routes.cars import cars_bp # getting Blueprint
    app.register_blueprint(cars_bp) # telling app about Blueprint

    return app # flask automatically finds function, then it can get something back
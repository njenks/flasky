from flask import Flask

def create_app():
    # __name__ stores the name of the module we're in
    app = Flask(__name__)

    from .routes.cars import cars_bp # getting Blueprint
    app.register_blueprint(cars_bp) # telling app about Blueprint

    return app # flask automatically finds function, then it can get something back
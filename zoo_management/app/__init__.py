from flask import Flask
from .db import db
from .routes.animals import animals_bp
from .routes.employees import employees_bp

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///zoo.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    app.register_blueprint(animals_bp, url_prefix='/animals')
    app.register_blueprint(employees_bp, url_prefix='/employees')

    with app.app_context():
        db.create_all()

    return app

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    
    db.init_app(app)
    
    from app.routes.animals import animals_bp
    from app.routes.employees import employees_bp
    
    app.register_blueprint(animals_bp)
    app.register_blueprint(employees_bp)
    
    return app

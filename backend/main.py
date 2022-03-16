import os
from flask import Flask
from config import Config

from routes.auth import auth_blueprint
from routes.user import user_blueprint
from database import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    app.register_blueprint(auth_blueprint, url_prefix='/api/v1')
    app.register_blueprint(user_blueprint, url_prefix='/api/v1')
    
    @app.route("/")
    @app.route("/api/v1/")
    def hello():
        return "Hello, World"

    return app

def setup_database(app):
    with app.app_context():
        db.create_all()

if __name__ == "__main__":
    app = create_app()
    if not os.path.isfile(app.config["SQLALCHEMY_DATABASE_URI"]):
      setup_database(app)
    app.run(debug=True)
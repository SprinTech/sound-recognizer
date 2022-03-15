from flask import Flask
from config import Config

from routes.auth import auth_blueprint
from routes.user import user_blueprint

app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(auth_blueprint, url_prefix='/api/v1')
app.register_blueprint(user_blueprint, url_prefix='/api/v1')

@app.route("/api/v1/")
def hello():
    return "Hello, World"

if __name__ == "__main__":
    app.run(debug=True)
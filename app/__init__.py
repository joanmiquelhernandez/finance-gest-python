from flask import Flask
from flask_jwt_extended import JWTManager

from app.config import config
from app.controllers import finance_bp
from app.models import init_db

def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config.from_object(config['development'])


    jwt = JWTManager(app)

    init_db()
    app.register_blueprint(finance_bp)

    return app

app = create_app()
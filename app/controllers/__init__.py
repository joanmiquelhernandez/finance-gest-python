from flask import Blueprint
from flask_restx import Api, Namespace
from app import dto

from app.controllers.auth_controller import auth_ns


finance_bp = Blueprint('api', __name__, url_prefix='/v1')

finance_api = Api(finance_bp, title='Finance Gest API', description='', version='0.0.1', doc='/doc')


finance_api.add_namespace(auth_ns)

finance_api.models[dto.error_schema.name] = dto.error_schema

def error(error_type: int, error_desc: str) -> dict:
    return {
        'error': {
            'error_type': error_type,
            'error_desc': error_desc
        }
    }

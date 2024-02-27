import base64
import os
from flask import request
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_restx import Namespace, Resource, marshal
from app import dto, logger
from werkzeug.security import check_password_hash, generate_password_hash

from app.models.user import User
from app.repositories.user_repository import UserRepo

log_error = logger.setup_logger(f'{__name__}_error', 'error.log')
log_info = logger.setup_logger(f'{__name__}_info', 'info.log')

auth_ns = Namespace('Authorization', path='/auth')

# dto
auth_ns.add_model(dto.user_dto.login_request.name, dto.user_dto.login_request)
auth_ns.add_model(dto.user_dto.login_response.name, dto.user_dto.login_response)
auth_ns.add_model(dto.user_dto.user_schema.name, dto.user_dto.user_schema)

# repos

user_repo = UserRepo()

@auth_ns.route('/login')
class Login(Resource):

    @auth_ns.expect(dto.user_dto.login_request)
    @auth_ns.marshal_with(dto.user_dto.login_response)
    def post(self):
        request_json = request.get_json()
        log_info.info(f'Peticion de Login con email "{request_json["email"]}"')

        user = user_repo.get_by_email(request_json['email'])

        if user:
            if check_password_hash(user.password, request_json['password']):
                image = None

                if user.profile_picture:
                    path_image  = os.getcwd() + f'/app/static/users/{user.alt_id}/profile_pictures/{user.profile_picture}'
                    with open(path_image, 'rb') as file:
                        image = base64.b64encode(file.read())

                return {
                    'access_token': create_access_token(identity=user.alt_id),
                    'refresh_token': create_refresh_token(identity=user.alt_id),
                    'user': {
                        'email': user.email,
                        'username': user.username,
                        'first_name': user.first_name,
                        'last_name': user.last_name,
                        'profile_picture': image,
                        'permission_level': user.role.permission
                    }
                }
            else:
                return {
                    'error': {
                        'error_type': 3,
                        'error_desc': 'Contraseña incorrectas'
                    }
                }
        else:
            return {
                'error': {
                    'error_type': 3,
                    'error_desc': 'Usuario no registrado'
                }
            }

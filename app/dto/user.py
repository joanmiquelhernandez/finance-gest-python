from flask_restx import Model, fields
from app.dto import error_schema

login_request = Model('LoginRequest', {
    'email'   : fields.String(description='Correo electrónico'),
    'password': fields.String(description='Contraseña'),
})

user_schema = Model('UserSchema', {
    'email'             : fields.String(),
    'username'          : fields.String(),
    'first_name'        : fields.String(),
    'last_name'         : fields.String(default=''),
    'profile_picture'   : fields.String(default='')
})


login_response = Model('LoginResponse', {
    'access_token'  : fields.String(description='Token usado para autenticar el usuario'),
    'refresh_token' : fields.String(description='Token usado para recordar'),
    'user'          : fields.Nested(user_schema),
    'error'         : fields.Nested(error_schema, required=False)
})

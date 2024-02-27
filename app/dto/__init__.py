from flask_restx import Model, fields


error_schema = Model('ErrorSchema', {
    'error_type': fields.Integer(description='Código identificador del error') ,
    'error_desc': fields.String(description='Descripción del error') ,
})


import app.dto.user as user_dto
from flask import request
from flask_restx import Resource
from app.routes import authentication_ns
from app import api, babel
import app.models.authentication as models

ERROR_MESSAGES = {
    'en': {
        'invalid_username': 'Invalid username',
        'invalid_password': 'Invalid password',
    },
    'es': {
        'invalid_username': 'Nombre de usuario inválido',
        'invalid_password': 'Contraseña inválida',
    }
}

@authentication_ns.route('/login')
class Login(Resource):
    @authentication_ns.expect(api.models[models.login_request_model.name])
    @authentication_ns.marshal_with(api.models[models.login_response_model.name], code=200)
    @authentication_ns.doc(
        responses={
            400: 'Validation error',
            403: 'Not authorized',
            500: 'Internal Server Error'
        },
    )
    def post(self):
        language = request.accept_languages.best_match(['en', 'es'])

        return {'message': ERROR_MESSAGES[language]['invalid_username']}, 404


@authentication_ns.route('/register')
class Register(Resource):
    @authentication_ns.expect(api.models[models.register_request_model.name])
    @authentication_ns.marshal_with(api.models[models.register_response_model.name])
    def post(self):
        pass
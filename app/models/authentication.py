from flask_restx import fields, Model
from app import api

login_request_model = Model('Login Request', {
    'email': fields.String(description='User email', required=True, example='example@email.com'),
    'password': fields.String(description='User password', required=True, example='mypassword')
})

login_response_model = Model('Login Response', {
    'id': fields.Integer(description='User ID'),
    'username': fields.String(description='User username'),
    'email': fields.String(description='User email'),
    'firstName': fields.String(description='User first Name'),
    'lastName': fields.String(description='User last Name'),
    'picture': fields.String(description='User raw profile picture')
})

register_request_model = Model('Register Request', {
    
})

register_response_model = Model('Register Response', {

})

api.models[login_request_model.name] = login_request_model
api.models[login_response_model.name] = login_response_model
api.models[register_request_model.name] = register_request_model
api.models[register_response_model.name] = register_response_model
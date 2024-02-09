from flask_restx import Namespace
from app import api

authentication_ns = api.namespace('Authentication', description='User authentication', path='/')

from .authentication import Login
from .authentication import Register
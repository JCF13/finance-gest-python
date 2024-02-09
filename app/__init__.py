import os
from flask import Flask, send_file, url_for
from flask_restx import Api, apidoc
from flask_babel import Babel
from app.config import Config

app = Flask(__name__, static_folder='static')
api = Api(app, version='1.0', title='Finance Gest API')
babel = Babel(app)

app.config.from_object(Config)

@app.route('/swaggerui/swagger-ui.css')
def custom_swagger_css():
    return send_file(os.path.join(app.root_path, 'static/css/custom_swagger_ui.css'))

@api.documentation
def custom_ui():
    return apidoc.ui_for(api)

from app.routes import authentication
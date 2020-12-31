import os

import click
from flask import Flask, render_template, jsonify, request
# 解决ajax请求的跨域问题
from flask_cors import CORS

from ui.apis.v1 import api_v1
from ui.blueprints.auth import auth_bp
from ui.blueprints.index import index_bp
from ui.blueprints.main import main_bp


def create_app(config_name=None):
    if config_name is not None:
        app = Flask(config_name)
    else:
        app = Flask('UI')
    CORS(app, supports_credentials=True)
    register_blueprints(app)
    return app


def register_blueprints(app):
    app.register_blueprint(index_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    # app.register_blueprint(todo_bp)
    # app.register_blueprint(home_bp)
    app.register_blueprint(api_v1, url_prefix='/api/v1')



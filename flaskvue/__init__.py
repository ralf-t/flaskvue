from urllib import response
from flask import Flask, current_app, jsonify
from os import environ


from flaskvue import (
    config,
    todo,
    user
)

from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity,
    create_access_token,
    set_access_cookies,
    verify_jwt_in_request,
    get_jwt
)


from flaskvue.extensions import (
    db,
    bcrypt,
    api,
    jwt,
    cors
)

def create_app():
    app = Flask(__name__)

    if environ['FLASK_ENV'] == 'development':
        app.config.from_object(config.DevelopmentConfig)

    register_extensions(app)
    register_blueprints(app)

    @app.post("/")
    def index():
        # return "hello world"
        return {'msg':'nice'}


    @app.post("/refresh")
    @jwt_required(refresh=True)
    def test():
        identity = get_jwt_identity()
        access_token = create_access_token(identity=identity)
        response = jsonify({'test':'test'})
        set_access_cookies(response, access_token)
        
        return response

    return app

def register_extensions(app):
    db.init_app(app)
    bcrypt.init_app(app)
    api.init_app(app)
    jwt.init_app(app)
    cors.init_app(app)

def register_blueprints(app):
    app.register_blueprint(todo.bp)
    app.register_blueprint(user.bp)
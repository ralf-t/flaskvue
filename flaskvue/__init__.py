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

    @app.post('/check-token')
    def check_token():
        try:
            verify_jwt_in_request()
            return {'msg':get_jwt_identity()}
        except:
            return {'msg':'hello'}

    @app.post("/refresh")
    @jwt_required(refresh=True)
    def test():
        identity = get_jwt_identity()
        access_token = create_access_token(identity=identity, fresh=False)
        response = jsonify({'test':'test'})
        set_access_cookies(response, access_token)
        
        return response

    @app.post("/protected-fresh")
    @jwt_required(fresh=True)
    def protected_fresh():
        identity = get_jwt_identity()
        response = jsonify({'user':identity})
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
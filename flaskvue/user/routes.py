import datetime
import json

from flask import jsonify

from flask.views import MethodView
from flask_jwt_extended.utils import set_access_cookies

from flask_smorest import abort

from flask_jwt_extended import (
    create_access_token, 
    jwt_required, 
    get_jwt_identity,
    create_refresh_token,
    unset_jwt_cookies,
    set_access_cookies,
    set_refresh_cookies,
    verify_jwt_in_request,
    get_jwt
)

from flask_cors import cross_origin

from flaskvue.extensions import bcrypt, db

from flaskvue.user import bp
from flaskvue.user.schemas import UserSchema
from flaskvue.user.validations import PutUserSchema, LoginSchema
from flaskvue.user.models import User

@bp.post("/post")
def postTest():
    return {1:1}

@bp.route("/login")
class Login(MethodView):
    
    
    @bp.arguments(LoginSchema)
    @bp.response(200)
    def post(self, data):

        username = data['username']
        password = data['password']
        # return username
        # if username != 'test' and password != 'test':
        #     abort(404, message="User not found.")

        access_token = create_access_token(identity=username)
        refresh_token = create_refresh_token(identity=username)
        
        response = jsonify({'test':'test'})
        set_access_cookies(response, access_token)
        set_refresh_cookies(response, refresh_token)
        # print(dir(response))
        # print(response.headers)
        # response.set_cookie("access", access_token)
        # response.set_cookie("refresh", refresh_token)
        return response
        # return jsonify(access_token=access_token, refresh_token=refresh_token)

@bp.post("/logout")
def logout():
    response = jsonify({"msg":"logout goods"})
    unset_jwt_cookies(response)
    return response


@bp.route("/protected")
class Protect(MethodView):

    @bp.arguments(LoginSchema)
    @bp.response(200)
    @jwt_required()
    def get(self, data):
        current_user = get_jwt_identity()
        print("current user",current_user)
        return jsonify(logged_in_as=current_user)

@bp.route("/")
class Users(MethodView):
    
    @bp.arguments(UserSchema, location="query")
    @bp.response(200, UserSchema(many=True))
    def get(self, args):
        return User.query.all()

    @bp.arguments(UserSchema)
    @bp.response(201, UserSchema)
    def post(self, data):
        user = User(
            username = data['username'],
            password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
        )

        db.session.add(user)
        db.session.commit()
        
        return user
    
    @bp.arguments(PutUserSchema)
    @bp.response(200, UserSchema)
    def put(self, data):
        user = fetch_user(data['id'])

        user.username = data['username']
        user.password = bcrypt.generate_password_hash(data['password']).decode('utf-8')

        db.session.commit()

        return user

@bp.route("/<id>")
class UsersByID(MethodView):
    
    @bp.response(200, UserSchema)
    def get(self, id):
        return fetch_user(id)


def fetch_user(user_id):
    '''
        Get user by ID
    '''
    user = User.query.get(user_id)
    if not user:
        abort(404, message="User not found.")
    return user
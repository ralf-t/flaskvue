from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_smorest import Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS

db = SQLAlchemy()
bcrypt = Bcrypt()
api = Api()
jwt = JWTManager()
cors = CORS()
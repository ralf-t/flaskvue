from flask_smorest import Blueprint
from flask_jwt_extended import (
    jwt_required,
    get_jwt,
    verify_jwt_in_request
)
bp = Blueprint('user', __name__, url_prefix="/user")
    

from flaskvue.user import models, routes
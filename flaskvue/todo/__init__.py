from flask_smorest import Blueprint

bp = Blueprint('todo', __name__, url_prefix="/user")

from flaskvue.todo import models
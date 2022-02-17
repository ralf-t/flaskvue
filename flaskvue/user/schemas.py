from marshmallow import Schema, fields, ValidationError, validates, validates_schema
from flaskvue.user.models import User

from flaskvue.todo.schemas import TodoSchema

class UserSchema(Schema):
    id = fields.Int(dump_only=True) # pang output lang to user, not for input
    username = fields.Str()
    todos = fields.Nested(TodoSchema, many=True)

    
from marshmallow import Schema, fields, ValidationError, validates, validates_schema
from flaskvue.user.models import User

class TodoSchema(Schema):
    id = fields.Int(dump_only=True)
    task = fields.Str()
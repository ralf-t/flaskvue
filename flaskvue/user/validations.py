
from marshmallow import Schema, fields, validates_schema, ValidationError
from flaskvue.user.models import User

class PutUserSchema(Schema):
    id = fields.Int(required=True)
    username = fields.Str()
    password = fields.Str()

    @validates_schema
    def validate_username(self, data, **kwargs):

        errors = {}

        id = data['id']
        print(id)
        username = data['username']
        
        if username:
            user = User.query.filter_by(username=username).first()
            
            # A different user uses the same username
            if user:
                if (user.id != id) and (user.username ==  username):
                    errors['username'] = ["Username is already taken."]
        
        if errors:
            raise ValidationError(errors)


class LoginSchema(Schema):
    
    username = fields.Str()
    password = fields.Str()

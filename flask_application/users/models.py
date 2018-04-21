from flask_security import UserMixin, RoleMixin
from flask_application.models import db, FlaskDocument

contract_status = ('In Progress', 'Completed')

class Role(FlaskDocument, RoleMixin):
    name = db.StringField(max_length=80, unique=True)
    description = db.StringField(max_length=255)


class User(FlaskDocument, UserMixin):
    email = db.StringField(max_length=255)
    username = db.StringField(max_length=255, unique=True)
    first_name = db.StringField(max_length=255)
    last_name = db.StringField(max_length=255)
    password = db.StringField(max_length=255)
    active = db.BooleanField(default=True)
    confirmed_at = db.DateTimeField()
    roles = db.ListField(db.ReferenceField(Role), default=[])

class Contract(FlaskDocument):
    contract_id = db.IntField(primary_key=True)
    author = db.ReferenceField(User, reverse_delete_rule=2)
    type = db.ListField(default=[])
    bidders = db.ListField(default=[])
    title = db.StringField(max_length=255)
    description = db.StringField(max_length=255)
    publishdate = db.DateTimeField()
    accepted_by = db.ReferenceField(User, reverse_delete_rule=2)
    accepted_date = db.DateTimeField()
    agreed_amount = db.StringField(max_length=255)
    status = db.StringField(choices=contract_status)

class Job(FlaskDocument):
    author = db.ReferenceField(User, reverse_delete_rule=2)
    type = db.ListField(default=[])
    title = db.StringField(max_length=255)
    description = db.StringField(max_length=255)
    publishdate = db.DateTimeField()
    accepted_by = db.ReferenceField(User, reverse_delete_rule=2)
    accepted_date = db.DateTimeField()
    agreed_amount = db.StringField(max_length=255)



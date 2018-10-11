from flask_app.db_init import db, FlaskDocument
from flask_app.models.user import User

class Job(FlaskDocument):
    author = db.ReferenceField(User, reverse_delete_rule=2)
    type = db.ListField(default=[])
    title = db.StringField(max_length=255)
    description = db.StringField(max_length=255)
    publishdate = db.DateTimeField()
    accepted_by = db.ReferenceField(User, reverse_delete_rule=2)
    accepted_date = db.DateTimeField()
    agreed_amount = db.StringField(max_length=255)
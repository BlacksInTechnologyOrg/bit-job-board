import datetime
from ..db_init import db, FlaskDocument


class Conversation(FlaskDocument):
    conversationId = db.StringField()
    participants = db.ListField()


class Message(FlaskDocument):
    conversationId = db.StringField()
    author = db.StringField()
    recipient = db.StringField()
    subject = db.StringField()
    content = db.StringField()
    created_at = db.DateTimeField(required=True, default=datetime.datetime.utcnow)
    modified_at = db.DateTimeField(required=True, default=datetime.datetime.utcnow)

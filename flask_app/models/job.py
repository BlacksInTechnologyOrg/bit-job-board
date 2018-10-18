import datetime
from bson import json_util
from flask_app.db_init import db, FlaskDocument
from flask_mongoengine import QuerySet
from flask_app.models.user import User


job_status = ('Open', 'Closed')


class CustomQuerySet(QuerySet):
    def to_json(self):
        return "[%s]" % (",".join([doc.to_json() for doc in self]))

class Job(FlaskDocument):
    author = db.ReferenceField(User, reverse_delete_rule=2, dbref=True)
    type = db.ListField(default=[])
    title = db.StringField(max_length=255)
    description = db.StringField(max_length=255)
    publishdate = db.DateTimeField(default=datetime.datetime.now())
    tags = db.ListField(default=[])
    status = db.StringField(choices=job_status)

    meta = {'queryset_class': CustomQuerySet,
            'indexes': [
                {'fields': ['$title', "$description"],
                 'default_language': 'english',
                 'weights': {'title': 10, 'description': 8}
                 }
            ]}

    def to_json(self):
        data = self.to_mongo()
        data["author"] = self.author.username
        return json_util.dumps(data)
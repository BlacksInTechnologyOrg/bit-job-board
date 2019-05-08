import datetime
import uuid
from bson import json_util
from flask_app.db_init import db, FlaskDocument
from flask_mongoengine import BaseQuerySet
from flask_app.models.user import User

job_status = ("Open", "Closed")


class CustomQuerySet(BaseQuerySet):
    def to_json(self):
        return "[%s]" % (",".join([doc.to_json() for doc in self]))


class Job(FlaskDocument):
    jobid = db.StringField(unique=True)
    author = db.StringField()
    type = db.ListField(default=[])
    title = db.StringField(max_length=255)
    description = db.StringField(max_length=255)
    content = db.StringField()
    publishdate = db.DateTimeField(default=datetime.datetime.now())
    tags = db.ListField(default=[])
    status = db.StringField(choices=job_status)

    # meta = {
    #     "queryset_class": CustomQuerySet,
    #     "indexes": [
    #         {
    #             "fields": ["$title", "$description", "$content"],
    #             "default_language": "english",
    #             "weights": {"title": 10, "description": 8, "content": 2},
    #         }
    #     ],
    # }

    def to_json(self):
        data = self.to_mongo()
        data.pop("_id")
        data["author"] = self.author.username
        return json_util.dumps(data)

    def save(self, *args, **kwargs):
        user = User.objects(username__exact=self.author).get()
        user.jobs.append(self.jobid)
        user.save()
        super(Job, self).save(*args, **kwargs)

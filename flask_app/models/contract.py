from flask_mongoengine import QuerySet
from bson import json_util
from flask_app.db_init import db, FlaskDocument
from flask_mongoengine import BaseQuerySet
from flask_app.models.user import User
from flask_app.utils import hashid

contract_status = ("In Progress", "Completed")


# class CustomQuerySet(BaseQuerySet):
#     def to_json(self):
#         return "[%s]" % (",".join([doc.to_json() for doc in self]))


class Contract(FlaskDocument):
    contractid = db.StringField(default=hashid(), unique=True)
    author = db.StringField()
    type = db.ListField(default=[])
    title = db.StringField(max_length=255)
    description = db.StringField(max_length=255)
    content = db.StringField()
    publishdate = db.DateTimeField()
    accepted_by = db.StringField()
    accepted_date = db.DateTimeField()
    ask_price = db.IntField()
    agreed_amount = db.IntField()
    tags = db.ListField(default=[])
    status = db.StringField(choices=contract_status, default="In Progress")

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

    # def to_json(self):
    #     data = self.to_mongo()
    #     data.pop("_id")
    #     data["author"] = self.author.username
    #     return json_util.dumps(data)

    def save(self, *args, **kwargs):
        user = User.objects(username__exact=self.author).get()
        user.contracts.append(self.contractid)
        user.save()
        super(Contract, self).save(*args, **kwargs)

from bson import json_util
from ..db_init import db, FlaskDocument
from flask_mongoengine import BaseQuerySet
from ..models.user import User

contract_status = ("In Progress", "Completed")


class CustomQuerySet(BaseQuerySet):
    def to_json(self):
        return "[%s]" % (",".join([doc.to_json() for doc in self]))


class ContractModel(FlaskDocument):
    contractid = db.StringField(unique=True)
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

    meta = {"queryset_class": CustomQuerySet, "collection": "contract"}

    def to_json(self):
        data = self.to_mongo()
        data.pop("_id")
        data["author"] = self.author.username
        return json_util.dumps(data)

    def save(self, *args, **kwargs):
        user = User.objects(username__exact=self.author).get()
        user.contracts.append(self.contractid)
        user.save()
        super(ContractModel, self).save(*args, **kwargs)

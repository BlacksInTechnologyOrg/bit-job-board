import logging
import datetime
import json
import os
import uuid
from flask_app.models.job import Job
from flask_app.models.user import User
from flask_app.models.contract import Contract
from mongoengine.queryset.visitor import Q
from mongoengine.errors import DoesNotExist
from elasticsearch_dsl import Search
from elasticsearch import Elasticsearch

log = logging.getLogger(__name__)


class JobClass:
    def create(self, author, title, description, content, tags=None):
        try:
            Job(
                jobid=uuid.uuid1().hex,
                author=User.objects.get(username=author).username,
                title=title,
                description=description,
                content=content,
                tags=tags,
                status="Open",
            ).save()
            return {"message": "Created Job"}
        except Exception:
            log.exception("Oops!")
            return {"message": "Something went wrong!"}

    def update(self, author, jobid, **kwargs):
        try:
            "Removing empty key value pairs"
            for k in list(kwargs.keys()):
                if not kwargs[k]:
                    kwargs.pop(k)

            Job.objects(author__exact=author).get_or_404(jobid=jobid).update(**kwargs)
            return {"message": "Updated Job"}
        except Exception:
            logging.exception("Oops!")
            return {"error": "Cannot not update Job!"}

    def delete(self, author, id):
        try:
            Job.objects(author__exact=author).get_or_404(jobid=id).delete()
            return {"message": "Job Deleted!"}
        except DoesNotExist:
            return {"message": f"Job ID {id} does not exist!"}
        except Exception:
            log.exception("Oops!")
            return {"message": "Something is wrong!"}


class ContractClass:
    def create(
        self, author, title, description, ask_price, content, agreed_amount=0, tags=None
    ):
        try:
            Contract(
                contractid=uuid.uuid1().hex,
                author=author,
                title=title,
                description=description,
                ask_price=ask_price,
                agreed_amount=agreed_amount,
                content=content,
                publishdate=datetime.datetime.utcnow().isoformat(" ", "seconds"),
                tags=tags,
                status="In Progress",
            ).save()

        except Exception:
            log.exception("Oops!")
            raise

    def update(self, author, contractid, **kwargs):
        try:
            for k in list(kwargs.keys()):
                if not kwargs[k]:
                    kwargs.pop(k)
            Contract.objects(author__exact=author).get(contractid=contractid).update(
                **kwargs
            )
            return {"message": "Updated Contract"}
        except DoesNotExist:
            logging.exception("Contract ID does not exist")
        except Exception:
            logging.exception("Cannot not update contract: " + contractid)
            return {"error": "Cannot not update contract!"}

    def delete(self, author, contractid):
        try:
            Contract.objects(author__exact=author).get(contractid=contractid).delete()
            return {"message": "Contract Deleted!"}
        except DoesNotExist:
            logging.exception("Contract ID does not exist")
            return {"message": f"Conttract ID {contractid} does not exist!"}
        except Exception:
            log.exception("Oops!")
            return {"message": "SOmething is wrong!"}

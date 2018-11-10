import logging
import datetime
import json
from flask_app.models.job import Job
from flask_app.models.user import User
from flask_app.models.contract import Contract
from mongoengine.queryset.visitor import Q
from mongoengine.errors import DoesNotExist

log = logging.getLogger(__name__)


class JobQuery:
    def search(self, jobid=None, search=None, **kwargs):
        try:
            if jobid is not None:
                js = Job.objects(jobid=jobid)
                return js.to_json() if js else "Job ID Does Not Exist"
            elif search is not None:
                return Job.objects.search_text(search).order_by("$text_score").to_json()
            else:
                queryargs = [
                    f"Q({kwkey}=User.objects.get(username='{kwval}'))"
                    if kwkey == "author"
                    else f"Q({kwkey}__contains='{kwval}')"
                    for kwkey, kwval in kwargs.items()
                    if kwval is not None
                ]
                queryargs = " | ".join(queryargs)
                doc = Job.objects(eval(queryargs))
                return doc.to_json()
        except Exception:
            log.exception("Oops!")

    def create(self, author, title, description, content, tags=None):
        try:
            Job(
                author=User.objects.get(username=author),
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
            "Removing "
            for k in list(kwargs.keys()):
                if not kwargs[k]:
                    kwargs.pop(k)

            Job.objects(author__exact=User.objects.get(username=author)).get_or_404(
                jobid=jobid
            ).update(**kwargs)
            return {"message": "Updated Job"}
        except Exception:
            logging.exception("Oops!")
            return {"error": "Cannot not update Job!"}

    def delete(self, author, id):
        try:
            Job.objects(author__exact=User.objects.get(username=author)).get_or_404(
                jobid=id
            ).delete()
            return {"message": "Job Deleted!"}
        except DoesNotExist:
            return {"message": f"Job ID {id} does not exist!"}
        except Exception:
            log.exception("Oops!")
            return {"message": "Something is wrong!"}


class ContractQuery:
    def create(
        self, author, title, description, ask_price, agreed_amount, content, tags=None
    ):
        try:
            Contract(
                author=User.objects.get(username=author),
                title=title,
                description=description,
                ask_price=ask_price,
                agreed_amount=agreed_amount,
                content=content,
                publishdate=datetime.datetime.utcnow().isoformat(" ", "seconds"),
                tags=tags,
                status="In Progress",
            ).save()

            return {"message": "Created Contract"}

        except Exception:
            log.exception("Oops!")

    def update(self, author, contractid, **kwargs):
        try:
            for k in list(kwargs.keys()):
                if not kwargs[k]:
                    kwargs.pop(k)
            Contract.objects(author__exact=User.objects.get(username=author)).get(
                contractid=contractid
            ).update(**kwargs)
            return {"message": "Updated Contract"}
        except Exception:
            logging.exception("Cannot not update contract: " + contractid)
            return {"error": "Cannot not update contract!"}

    def search(self, contractid=None, **kwargs):
        if contractid is not None:
            js = Contract.objects(contractid=contractid)
            return js.to_json() if js else "Contract ID Does Not Exist"

        if len(kwargs) == 0:
            return Contract.objects().to_json()
        elif "search" in kwargs and kwargs["search"] is not None:
            print(kwargs["search"])
            print(
                Contract.objects.search_text(kwargs["search"]).order_by("$text_score")
            )
            return Contract.objects.search_text(kwargs["search"]).order_by(
                "$text_score"
            )
        else:
            queryargs = [
                f"Q({kwkey}=User.objects.get(username='{kwval}'))"
                if kwkey == "author"
                else f"Q({kwkey}__contains='{kwval}')"
                for kwkey, kwval in kwargs.items()
                if kwval is not None
            ]
            queryargs = " | ".join(queryargs)
            doc = Contract.objects(eval(queryargs))
            return json.loads(doc.to_json())

    def delete(self, author, contractid):
        try:
            Contract.objects(
                author__exact=User.objects.get(username=author)
            ).get_or_404(contractid=contractid).delete()
            return {"message": "Contract Deleted!"}
        except DoesNotExist:
            logging.exception("Contract ID does not exist")
            return {"message": f"Conttract ID {contractid} does not exist!"}
        except Exception:
            log.exception("Oops!")
            return {"message": "SOmething is wrong!"}

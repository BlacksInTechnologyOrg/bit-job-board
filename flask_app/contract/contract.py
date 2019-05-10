import logging
import datetime
import uuid
from flask_app.models.contractmodel import ContractModel
from mongoengine.errors import DoesNotExist

log = logging.getLogger(__name__)


class Contract:
    def create(
        self, author, title, description, ask_price, content, agreed_amount=0, tags=None
    ):
        try:
            ContractModel(
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
            ContractModel.objects(author__exact=author).get(
                contractid=contractid
            ).update(**kwargs)
            return {"message": "Updated Contract"}
        except DoesNotExist:
            logging.exception("Contract ID does not exist")
        except Exception:
            logging.exception("Cannot not update contract: " + contractid)
            return {"error": "Cannot not update contract!"}

    def delete(self, author, contractid):
        try:
            ContractModel.objects(author__exact=author).get(
                contractid=contractid
            ).delete()
            return {"message": "Contract Deleted!"}
        except DoesNotExist:
            logging.exception("Contract ID does not exist")
            return {"message": f"Conttract ID {contractid} does not exist!"}
        except Exception:
            log.exception("Oops!")
            return {"message": "SOmething is wrong!"}

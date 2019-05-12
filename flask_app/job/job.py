import logging
import uuid
from ..models.jobmodel import JobModel
from ..models.user import User
from mongoengine.errors import DoesNotExist

log = logging.getLogger(__name__)


class Job:
    def create(self, author, title, description, content, tags=None):
        try:
            JobModel(
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

            JobModel.objects(author__exact=author).get_or_404(jobid=jobid).update(
                **kwargs
            )
            return {"message": "Updated Job"}
        except Exception:
            logging.exception("Oops!")
            return {"error": "Cannot not update Job!"}

    def delete(self, author, id):
        try:
            JobModel.objects(author__exact=author).get_or_404(jobid=id).delete()
            return {"message": "Job Deleted!"}
        except DoesNotExist:
            return {"message": f"Job ID {id} does not exist!"}
        except Exception:
            log.exception("Oops!")
            return {"message": "Something is wrong!"}

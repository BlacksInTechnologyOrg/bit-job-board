import logging
import datetime
from flask_app.models.job import Job
from flask_app.models.user import User
from flask_app.models.contract import Contract
from mongoengine.queryset.visitor import Q
from mongoengine.errors import DoesNotExist

log = logging.getLogger(__name__)


class JobQuery:
    def create(self, author, title, description, content, tags=None):
        try:
            Job(author=User.objects.get(username=author),
                title=title,
                description=description,
                content=content,
                publishdate=datetime.datetime.utcnow().isoformat(' ', 'seconds'),
                tags=tags,
                status='Open'
                ).save()
            return {'message': 'Created Job'}
        except:
            log.exception('Oops!')
            return {'message': 'Something went wrong!'}

    def search(self, search=None, **kwargs):
        try:
            if len(kwargs) == 0:
                return Job.objects().to_json()
            elif search is not None:
                return Job.objects.search_text(search).order_by('$text_score').to_json()
            else:
                queryargs = [
                    f"Q({kwkey}=User.objects.get(username='{kwval}'))" if kwkey == 'author' else f"Q({kwkey}__contains='{kwval}')"
                    for kwkey, kwval in kwargs.items() if kwval is not None]
                queryargs = " | ".join(queryargs)
                doc = Job.objects(eval(queryargs))
                return doc.to_json()
        except:
            log.exception('Oops!')

    def delete(self, author, id):
        try:
            author = author if author == User.objects.get(username=author) else None
            Job.objects(author__exact=User.objects.get(username=author)).get_or_404(id=id).delete()
            return {'message': 'Job Deleted!'}
        except DoesNotExist:
            return {'message': f'Job ID {id} does not exist!'}
        except:
            log.exception('Oops!')
            return {'message': 'SOmething is wrong!'}

class ContractQuery:
    def create(self, author, title, description, price, content, tags=None):
        try:
            Contract(author=User.objects.get(username=author),
                     title=title,
                     description=description,
                     ask_price=price,
                     content=content,
                     publishdate=datetime.datetime.utcnow().isoformat(' ', 'seconds'),
                     tag=tags,
                     status='Open'
                     ).save()

        except:
            log.exception('Oops!')

    def search(self, search=None, **kwargs):
        if len(kwargs) == 0:
            return Job.objects().to_json()
        elif search is not None:
            return Job.objects.search_text(search).order_by('$text_score').to_json()
        else:
            queryargs = [
                f"Q({kwkey}=User.objects.get(username='{kwval}'))" if kwkey == 'author' else f"Q({kwkey}__contains='{kwval}')"
                for kwkey, kwval in kwargs.items() if kwval is not None]
            queryargs = " | ".join(queryargs)
            doc = Job.objects(eval(queryargs))
            return doc.to_json()

    def delete(self, author, id):
        try:
            author = author if author == User.objects.get(username=author) else None
            Contract.objects(author__exact=User.objects.get(username=author)).get_or_404(id=id).delete()
            return {'message': 'Job Deleted!'}
        except DoesNotExist:
            return {'message': f'Job ID {id} does not exist!'}
        except:
            log.exception('Oops!')
            return {'message': 'SOmething is wrong!'}

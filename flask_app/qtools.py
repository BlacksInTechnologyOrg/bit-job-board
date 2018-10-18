from flask_app.models.job import Job
from flask_app.models.user import User
from flask_app.models.contract import Contract
from mongoengine.queryset.visitor import Q

class JobQuery():
    def search(self, search=None, **kwargs):
        if len(kwargs) == 0:
            return Job.objects().to_json()
        elif search is not None:
            return Job.objects.search_text(search).order_by('$text_score').to_json()
        else:
            queryargs = [f"Q({kwkey}=User.objects.get(username='{kwval}'))" if kwkey == 'author' else f"Q({kwkey}__contains='{kwval}')" for kwkey, kwval in kwargs.items() if kwval is not None]
            queryargs = " | ".join(queryargs)
            doc = Job.objects(eval(queryargs))
            return doc.to_json()

class ContractQuery():
    def search(self, search=None, **kwargs):
        if len(kwargs) == 0:
            return Job.objects().to_json()
        elif search is not None:
            return Job.objects.search_text(search).order_by('$text_score').to_json()
        else:
            queryargs = [f"Q({kwkey}=User.objects.get(username='{kwval}'))" if kwkey == 'author' else f"Q({kwkey}__contains='{kwval}')" for kwkey, kwval in kwargs.items() if kwval is not None]
            queryargs = " | ".join(queryargs)
            doc = Job.objects(eval(queryargs))
            return doc.to_json()


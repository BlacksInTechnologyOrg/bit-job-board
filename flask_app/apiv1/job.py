from flask import request
from flask_restplus import Resource, Namespace
from flask_app.qtools import JobQuery

jobapi = Namespace('Jobs', description='Jobs Api')


@jobapi.route('/')
class Jobs(Resource):
    @jobapi.doc(params={'search': 'Search', 'author': 'Publisher', 'title': 'Job Title'})
    def get(self):
        if len(request.args) == 0:
            return JobQuery().search()
        else:
            return JobQuery().search(search=request.args.get('search'),
                                     author=request.args.get('author'),
                                     title=request.args.get('title'))
        # return {'message': 'Created Jobs'}

    def post(self):
        return {'message': 'Created Jobs'}

    def delete(self):
        return {'message': 'Deleted Jobs'}


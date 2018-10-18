from flask import request
from flask_restplus import Resource, Namespace
from flask_app.qtools import ContractQuery

contractapi = Namespace('Contracts', description='Contracts Api')


@contractapi.route('/')
class Contracts(Resource):
    @contractapi.doc(params={'search': 'Search', 'author': 'Author', 'title': 'Job Title', 'status': 'Status'})
    def get(self):
        if len(request.args) == 0:
            return ContractQuery().search()
        else:
            return ContractQuery().search(search=request.args.get('search'),
                                     author=request.args.get('author'),
                                     title=request.args.get('title'),
                                          status=request.args.get('status'))

    def post(self):
        return {'message': 'Created contract'}

    def delete(self):
        return {'message': 'Deleted contract'}


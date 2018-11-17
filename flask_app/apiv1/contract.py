import json
from flask import request, jsonify
from flask_restplus import Resource, Namespace, fields
from flask_app.qtools import ContractQuery

contractapi = Namespace("Contracts", description="Contracts Api")

contracts = contractapi.model(
    "Contracts",
    {
        "title": fields.String(required=True, description="Title"),
        "description": fields.String(required=True, description="Description"),
        "content": fields.String(required=True, description="Content"),
        "ask_price": fields.String(required=True, description="Ask Price"),
        "tags": fields.String(
            required=True, description="Tags comma-separated", example="a,b,c"
        ),
    },
)


@contractapi.route("/")
class Contracts(Resource):
    @contractapi.doc(
        params={
            "search": "Search",
            "author": "Author",
            "title": "Job Title",
            "status": "Status",
        }
    )
    def get(self):
        print(request.args.to_dict())
        if len(request.args) == 0:
            return ContractQuery().search()
        else:
            respdict = ContractQuery().search(**request.args.to_dict())
            print(respdict)
            return respdict

    @contractapi.expect(contracts)
    def post(self):
        data = json.loads(contractapi.payload)
        return ContractQuery().create(
            author=data["author"],
            title=data["title"],
            description=data["description"],
            content=data["content"],
            ask_price=data["ask_price"],
            agreed_amount=data["agreed_amount"],
            tags=data["tags"],
        )


@contractapi.route("/<string:contractid>")  # noqa: F811
class Contracts(Resource):
    def get(self, contractid):
        print(contractid)
        respdict = ContractQuery().search(contractid=contractid)
        print(respdict)
        return respdict

    @contractapi.expect(contracts)
    def put(self, contractid):
        data = json.loads(contractapi.payload)
        return ContractQuery().update(
            author="matt",
            contractid=contractid,
            title=data["title"],
            description=data["description"],
            ask_price=data["ask_price"],
            content=data["content"],
            tags=data["tags"],
        )

    def delete(self, contractid):
        return ContractQuery().delete("matt", contractid)

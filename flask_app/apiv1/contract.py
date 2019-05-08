import json
import logging
from flask import request, jsonify
from flask_restplus import Resource, Namespace, fields

# from flask_app.qtools import ContractQuery
from flask_app.search.contract import ContractQuery
from flask_app.qtools import ContractClass
from flask_jwt_extended import current_user, jwt_required

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
        try:
            print(request.args.to_dict())
            # if len(request.args) == 0:
            #     return ContractQuery().search()
            # else:
            #     # respdict = ContractQuery().search(**request.args.to_dict())
            #     hits = ContractQuery().search(1,100)
            #     return jsonify(hits)
            hits = ContractQuery().search(1, 100, **request.args.to_dict())
            return jsonify(hits)
        except Exception:
            logging.exception("Error Getting Contracts")
            return {"message": "Error Getting Contracts"}

    # @jwt_required
    @contractapi.expect(contracts)
    def post(self):
        try:
            data = contractapi.payload
            ContractClass().create(
                author=data["author"],
                title=data["title"],
                description=data["description"],
                content=data["content"],
                ask_price=data["ask_price"],
                tags=data["tags"],
            )
            return {"message": "Created Contract"}
        except Exception:
            logging.exception("Error creating Contract Offer")
            return {"message": "Error creating Contract Offer"}


@contractapi.route("/<string:contractid>")  # noqa: F811
class Contracts(Resource):
    def get(self, contractid):
        print(contractid)
        respdict = ContractQuery().search(contractid=contractid)
        print(respdict)
        return respdict

    @contractapi.expect(contracts)
    def put(self, contractid):
        try:
            data = json.loads(contractapi.payload)
            ContractClass().update(
                author="matt",
                contractid=contractid,
                title=data["title"],
                description=data["description"],
                ask_price=data["ask_price"],
                content=data["content"],
                tags=data["tags"],
            )
            return {"message": "Updated Contract"}
        except Exception:
            logging.exception("Error updating Contract: " + contractid)
            return {"message": f"Error updating Contract: {contractid}"}

    def delete(self, contractid):
        return ContractClass().delete("matt", contractid)

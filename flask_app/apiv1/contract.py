import json
import logging
import urllib.parse
from flask import request, jsonify
from flask_restplus import Resource, Namespace, fields
from flask_app.contract.contractquery import ContractQuery
from flask_app.contract.contract import Contract

log = logging.getLogger(__name__)

contractapi = Namespace("Contracts", description="Contracts Api")

contracts = contractapi.model(
    "Contracts",
    {
        "title": fields.String(required=True, description="Title"),
        "description": fields.String(required=True, description="Description"),
        "content": fields.String(required=True, description="Content"),
        "ask_price": fields.String(required=True, description="Ask Price"),
        "tags": fields.List(
            fields.String(required=True, description="Tags comma-separated")
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
            hits = ContractQuery().search(1, 100, **request.args.to_dict())
            return jsonify(hits)
        except Exception:
            logging.exception("Error Getting Contracts")
            return {"message": "Error Getting Contracts"}

    # @jwt_required
    @contractapi.expect(contracts)
    def post(self):
        try:
            data = json.loads(contractapi.payload)
            Contract().create(
                author=data["author"],
                title=data["title"],
                description=urllib.parse.unquote(data["description"]),
                content=urllib.parse.unquote(data["content"]),
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
        try:
            log.debug(contractid)
            resp = ContractQuery().search(1, 100, contractid=contractid)
            log.debug(resp)
            if resp:
                return resp
            else:
                return jsonify({"message": "Contract ID Does Not Exist"})
        except Exception:
            log.exception("Error Getting Contract: " + contractid)
            return {"message": f"Error Getting {contractid}"}

    @contractapi.expect(contracts)
    def put(self, contractid):
        try:
            data = json.loads(contractapi.payload)
            Contract().update(
                author="matt",
                contractid=contractid,
                title=data["title"],
                description=urllib.parse.unquote(data["description"]),
                content=urllib.parse.unquote(data["content"]),
                ask_price=data["ask_price"],
                tags=data["tags"],
            )
            return {"message": "Updated Contract"}
        except Exception:
            logging.exception("Error updating Contract: " + contractid)
            return {"message": f"Error updating Contract: {contractid}"}

    def delete(self, contractid):
        return Contract().delete("matt", contractid)

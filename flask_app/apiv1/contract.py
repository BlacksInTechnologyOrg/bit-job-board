from flask import request
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
        if len(request.args) == 0:
            return ContractQuery().search()
        else:
            return ContractQuery().search(
                search=request.args.get("search"),
                author=request.args.get("author"),
                title=request.args.get("title"),
                status=request.args.get("status"),
            )

    @contractapi.expect(contracts)
    def post(self):
        data = contractapi.payload
        tags = data["tags"].split(",")
        return ContractQuery().create(
            author=data["author"],
            title=data["title"],
            description=data["description"],
            content=data["content"],
            ask_price=data["ask_price"],
            tags=tags,
        )


@contractapi.route("/<contractid>")  # noqa: F811
class Contracts(Resource):
    def get(self, contractid):
        if contractid:
            return ContractQuery().search(contractid=contractid)

    @contractapi.expect(contracts)
    def post(self):
        data = contractapi.payload
        tags = data["tags"].split(",")
        return ContractQuery().create(
            author=data["author"],
            title=data["title"],
            description=data["description"],
            content=data["content"],
            ask_price=data["ask_price"],
            tags=tags,
        )

    @contractapi.expect(contracts)
    def put(self, contractid):
        data = contractapi.payload
        return ContractQuery().update(
            author="joe",
            contractid=contractid,
            title=data["title"],
            description=data["description"],
            ask_price=data["ask_price"],
            content=data["content"],
            tags=data["tags"],
        )

    @contractapi.doc(params={"id": "Job Id"})
    def delete(self, contractid):
        return ContractQuery().delete("joe", contractid)

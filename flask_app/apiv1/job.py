import json
from flask import request
from flask_restplus import Resource, Namespace, fields
from flask_app.qtools import JobQuery

jobapi = Namespace("Jobs", description="Jobs Api")

jobs = jobapi.model(
    "Jobs",
    {
        "author": fields.String(required=True, description="Author"),
        "title": fields.String(required=True, description="Title"),
        "description": fields.String(required=True, description="Description"),
        "content": fields.String(required=True, description="Content"),
        "tags": fields.String(
            required=True, description="Tags comma-separated", example="a,b,c"
        ),
    },
)


@jobapi.route("/")
class Jobs(Resource):
    @jobapi.doc(
        params={"search": "Search", "author": "Publisher", "title": "Job Title"}
    )
    def get(self):
        return JobQuery().search(
            search=request.args.get("search"),
            author=request.args.get("author"),
            title=request.args.get("title"),
        )

    @jobapi.expect(jobs)
    def post(self):
        data = jobapi.payload
        data = json.loads(data)
        return JobQuery().create(
            author=data["author"],
            title=data["title"],
            description=data["description"],
            content=data["content"],
            tags=data["tags"],
        )


@jobapi.route("/<string:jobid>")  # noqa: F811
class Jobs(Resource):
    def get(self, jobid):
        if jobid:
            return JobQuery().search(jobid=jobid)

    @jobapi.expect(jobs)
    def put(self, jobid):
        data = jobapi.payload
        data = json.loads(data)
        return JobQuery().update(
            author="matt",
            jobid=jobid,
            title=data["title"],
            description=data["description"],
            content=data["content"],
            tags=data["tags"],
            status=data["status"],
        )

    def delete(self, jobid):
        return JobQuery().delete("matt", jobid)

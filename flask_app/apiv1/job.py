import json
import logging
import urllib.parse
from flask import request, jsonify
from flask_restplus import Resource, Namespace, fields
from flask_app.search.job import JobQuery
from flask_app.qtools import JobClass

log = logging.getLogger(__name__)


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
        params={
            "description": "Description",
            "author": "Publisher",
            "title": "Job Title",
        }
    )
    def get(self):
        try:
            print(request.args.to_dict())
            hits = JobQuery().search(1, 100, **request.args.to_dict())
            return jsonify(hits)
        except Exception:
            log.exception("Error Getting Contracts")
            return {"message": "Error Getting Contracts"}

    @jobapi.expect(jobs)
    def post(self):
        data = json.loads(jobapi.payload)
        return JobClass().create(
            author=data["author"],
            title=data["title"],
            description=urllib.parse.unquote(data["description"]),
            content=urllib.parse.unquote(data["content"]),
            tags=data["tags"],
        )


@jobapi.route("/<string:jobid>")  # noqa: F811
class Jobs(Resource):
    def get(self, jobid):
        try:
            log.debug(jobid)
            resp = JobQuery().search(1, 100, jobid=jobid)
            log.debug(resp)
            if resp:
                return resp
            else:
                return jsonify({"message": "Job ID Does Not Exist"})
        except Exception:
            return {"message": f"Error Getting {jobid}"}

    @jobapi.expect(jobs)
    def put(self, jobid):
        data = jobapi.payload
        data = json.loads(data)
        return JobClass().update(
            author="matt",
            jobid=jobid,
            title=data["title"],
            description=urllib.parse.unquote(data["description"]),
            content=urllib.parse.unquote(data["content"]),
            tags=data["tags"],
            status=data["status"],
        )

    def delete(self, jobid):
        return JobClass().delete("matt", jobid)

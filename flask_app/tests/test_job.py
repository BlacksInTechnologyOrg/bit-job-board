import json
import pytest
from ..models.user import User
from ..models.jobmodel import JobModel
from mongoengine.errors import DoesNotExist


# def test_searchJobByJobId(client):
#     jid = Job.objects.get(title__exact="Job2").jobid
#     print(jid)
#     rv = client.get("/api/Jobs/" + jid)
#     assert jid.encode("utf-8") in rv.data
#
#
# def test_searchJobByJobId_JobDoesNotExist(client):
#     rv = client.get("/api/Jobs/randomID")
#     assert b'{"message":"Job ID Does Not Exist"}\n' in rv.data


def test_createJob(client):
    data = dict(
        author="matt",
        title="Test",
        description="Test Job",
        content="This is a job made during test",
        tags=["some", "random", "tag"],
        status="Open",
    )
    js = json.dumps(data)
    resp = client.post(
        "/api/Jobs/", data=js, content_type="application/json", follow_redirects=True
    )
    testjob = JobModel.objects.get(title="Test")
    assert b'{"message": "Created Job"}' in resp.data
    for val in data:
        assert data[val] == testjob[val]


def test_updateJob(client):
    data = dict(
        author="matt",
        title="UpdatedTitle",
        description="UpdatedDescription",
        content="",
        tags=[],
        status="",
    )
    js = json.dumps(data)
    jobid = JobModel.objects(author="matt").get(title="Job1").jobid
    resp = client.put(
        f"/api/Jobs/{jobid}",
        data=js,
        content_type="application/json",
        follow_redirects=True,
    )
    testjob = JobModel.objects(author="matt").get(title="UpdatedTitle")
    assert b'{"message": "Updated Job"}' in resp.data
    assert data["title"] == testjob["title"]
    assert data["description"] == testjob["description"]


def test_deleteJob(client):
    jobid = JobModel.objects(author="matt").get(title="Job1").jobid
    resp = client.delete(f"/api/Jobs/{jobid}")
    with pytest.raises(DoesNotExist):
        JobModel.objects(author="matt").get(jobid=jobid)
    assert b'{"message": "Job Deleted!"}' in resp.data

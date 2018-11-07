import json
import pytest
from flask_app.models.user import User
from flask_app.models.job import Job
from mongoengine.errors import DoesNotExist


def test_searchJobByJobId(client):
    jid = Job.objects.get(author=User.objects.get(username="matt")).jobid
    rv = client.get("/api/Jobs/" + jid)
    assert jid.encode("utf-8") in rv.data


def test_searchJobByJobId_JobDoesNotExist(client):
    rv = client.get("/api/Jobs/randomID")
    assert b"Job ID Does Not Exist" in rv.data


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
    resp = client.post("/api/Jobs/", json=js, follow_redirects=True)
    testjob = (
        Job.objects(author=User.objects.get(username="matt"))
        .get(title="Test")
        .to_json()
    )
    tj = json.loads(testjob)
    assert b'{"message": "Created Job"}' in resp.data
    for k in data:
        assert data[k] == tj[k]


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
    jobid = (
        Job.objects(author=User.objects.get(username="matt")).get(title="Job1").jobid
    )
    resp = client.put(f"/api/Jobs/{jobid}", json=js, follow_redirects=True)
    testjob = Job.objects(author=User.objects.get(username="matt")).to_json()
    assert b'{"message": "Updated Job"}' in resp.data
    assert data["title"] in testjob
    assert data["description"] in testjob


def test_deleteJob(client):
    jobid = (
        Job.objects(author=User.objects.get(username="matt")).get(title="Job1").jobid
    )
    resp = client.delete(f"/api/Jobs/{jobid}")
    with pytest.raises(DoesNotExist):
        Job.objects(author=User.objects.get(username="matt")).get(jobid=jobid)
    assert b'{"message": "Job Deleted!"}' in resp.data

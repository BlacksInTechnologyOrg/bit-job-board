import json
import pytest
from flask_app.models.user import User
from flask_app.models.contract import Contract
from mongoengine.errors import DoesNotExist
from mongoengine import connect


# def test_searchContractByContractId(client):
#     jid = Contract.objects.get(author=User.objects.get(username="matt")).title
#     rv = client.get(f"/api/Contracts/{jid}")
#     assert jid.encode("utf-8") in rv.data
#
#
# def test_searchContractByContractId_ContractDoesNotExist(client):
#     rv = client.get("/api/Contracts/randomID")
#     assert b'{"message":"Contract ID Does Not Exist"}\n' in rv.data


def test_createContract(client):
    data = dict(
        author="matt",
        title="Test",
        description="Test Contract",
        content="This is a Contract made during test",
        tags=["some", "random", "tag"],
        status="In Progress",
        ask_price=50,
    )
    js = json.dumps(data)
    resp = client.post("/api/Contracts/", json=js, follow_redirects=True)
    testContract = Contract.objects.get(title="Test")
    assert b'{"message": "Created Contract"}' in resp.data
    for k in data:
        assert data[k] == testContract[k]


def test_updateContract(client):
    data = dict(
        author="matt",
        title="UpdatedTitle",
        description="UpdatedDescription",
        ask_price="",
        content="",
        tags=[],
        status="",
    )
    js = json.dumps(data)
    contractid = Contract.objects(author="matt").get(title="Contract1").contractid
    resp = client.put(f"/api/Contracts/{contractid}", json=js, follow_redirects=True)
    testContract = Contract.objects(author="matt").get(title="UpdatedTitle")
    assert b'{"message": "Updated Contract"}' in resp.data
    assert data["title"] == testContract["title"]
    assert data["description"] == testContract["description"]


def test_deleteContract(client):
    contractid = Contract.objects(author="matt").get(title="Contract1").contractid
    resp = client.delete(f"/api/Contracts/{contractid}")
    with pytest.raises(DoesNotExist):
        Contract.objects(author="matt").get(contractid=contractid)
    assert b'{"message": "Contract Deleted!"}' in resp.data

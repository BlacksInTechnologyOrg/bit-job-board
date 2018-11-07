import json
import pytest
from flask_app.models.user import User
from flask_app.models.contract import Contract
from mongoengine.errors import DoesNotExist


def test_searchContractByContractId(client):
    jid = Contract.objects.get(author=User.objects.get(username="joe")).contractid
    print(jid)
    rv = client.get(f"/api/Contracts/{jid}")
    assert jid.encode("utf-8") in rv.data


def test_searchContractByContractId_ContractDoesNotExist(client):
    rv = client.get("/api/Contracts/randomID")
    assert b"Contract ID Does Not Exist" in rv.data


def test_createContract(client):
    data = dict(
        author="matt",
        title="Test",
        description="Test Contract",
        content="This is a Contract made during test",
        tags=["some", "random", "tag"],
        status="In Progress",
        ask_price=50,
        agreed_amount=50,
    )
    js = json.dumps(data)
    resp = client.post("/api/Contracts/", json=js, follow_redirects=True)
    testContract = (
        Contract.objects(author=User.objects.get(username="matt"))
        .get(title="Test")
        .to_json()
    )
    tc = json.loads(testContract)
    assert b'{"message": "Created Contract"}' in resp.data
    for k in data:
        assert data[k] == tc[k]


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
    contractid = (
        Contract.objects(author=User.objects.get(username="matt"))
        .get(title="Contract1")
        .contractid
    )
    resp = client.put(f"/api/Contracts/{contractid}", json=js, follow_redirects=True)
    testContract = json.loads(
        Contract.objects(author=User.objects.get(username="matt")).to_json()
    )
    assert b'{"message": "Updated Contract"}' in resp.data
    assert data["title"] == testContract[0]["title"]
    assert data["description"] == testContract[0]["description"]


def test_deleteContract(client):
    contractid = (
        Contract.objects(author=User.objects.get(username="matt"))
        .get(title="Contract1")
        .contractid
    )
    print(contractid)
    resp = client.delete(f"/api/Contracts/{contractid}")
    with pytest.raises(DoesNotExist):
        Contract.objects(author=User.objects.get(username="matt")).get(
            contractid=contractid
        )
    assert b'{"message": "Contract Deleted!"}' in resp.data

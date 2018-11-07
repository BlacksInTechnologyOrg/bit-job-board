import pytest
import logging
from flask import current_app
from flask_app import create_app
from flask_app.models.user import User
from flask_app.db_init import db
from flask_app.script import PopulateDB, ResetDB


@pytest.fixture
def client():
    jbapp = create_app(config_name="testing")
    client = jbapp.test_client()
    ResetDB().drop_collections()
    PopulateDB().create_users()
    PopulateDB.create_jobs()
    PopulateDB.create_contracts()

    ctx = jbapp.app_context()
    ctx.push()
    yield client
    ctx.pop()

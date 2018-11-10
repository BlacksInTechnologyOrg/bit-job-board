import datetime
import logging
from flask import json
from flask_app.db_init import FlaskDocument
from flask_app.models.user import User
from flask_app.models.job import Job
from flask_app.models.contract import Contract
from flask_app.messaging import MessageHandler
from flask_app.apiv1 import api


def register(app):
    @app.cli.command()
    def resetdb():
        ResetDB().run()

    @app.cli.command()
    def populatedb():
        PopulateDB().run()

    @app.cli.command()
    def createMessages():
        Message().run()

    # @app.cli.command()
    # def getPostmanCollection():
    #     Postman().run()


class ResetDB:
    """Drops all tables and recreates them"""

    def run(self):
        self.drop_collections()

    def drop_collections(self):
        for klass in FlaskDocument.all_subclasses():
            klass.drop_collection()


class PopulateDB:
    """Fills in predefined data to DB"""

    def run(self):
        try:
            self.create_users()
            self.create_jobs()
            self.create_contracts()
        except Exception:
            logging.exception("Database contains data, resetting")
            ResetDB().drop_collections()

    @staticmethod
    def create_users():
        users = []
        for u in (
            ("matt", "matt@lp.com", "password", ["admin"], True, "Matt", "Jenkins"),
            ("joe", "joe@lp.com", "password", ["editor"], True, "Joe", "Jackson"),
            ("joey", "joey@lp.com", "password", ["editor"], True, "Joey", "Jackson"),
            ("jill", "jill@lp.com", "password", ["author"], True, "Jill", "Jane"),
            ("tiya", "tiya@lp.com", "password", [], False, "Tiya", "Willams"),
            ("dubh3124", "dubh3124@lp.com", "password", [], True, "Herman", "Haggerty"),
        ):
            user = User(
                username=u[0],
                email=u[1],
                password=User().generate_hash(u[2]),
                active=u[4],
                firstname=u[5],
                lastname=u[6],
            )
            users.append(user)

        User.objects.insert(users)

    @staticmethod
    def create_jobs():
        for title, description, author, status in (
            ("Job1", "Programmer", "matt", "Open"),
            ("Job2", "System Administrator", "joe", "Closed"),
            ("Job3", "Programmer", "joe", "Open"),
        ):
            user = User.objects

            test = Job
            test(
                author=user.get(username=author),
                title=title,
                description=description,
                publishdate=datetime.datetime.utcnow().isoformat(" ", "seconds"),
                status=status,
            ).save()

    @staticmethod
    def create_contracts():
        for title, description, content, author, status, ask_price, agreed_amount in (
            ("Contract1", "Web Design", "content", "matt", "In Progress", 50, 50),
            ("Contract2", "Data Mining", "content", "joe", "Completed", 323, 300),
            ("Contract3", "Dashboard", "content", "joe", "In Progress", 132, 120),
        ):
            user = User.objects

            test = Contract
            test(
                author=user.get(username=author),
                title=title,
                description=description,
                content=content,
                status=status,
                ask_price=ask_price,
                agreed_amount=agreed_amount,
            ).save()


class Message:
    def run(self):
        self.createMesages()

    def createMesages(self):
        i = 0
        while i < 10:
            MessageHandler().newMessage("dubh3124", "joe", "test", "testing")
            i += 1


class Postman:
    def run(self):
        self.getPostmanCollection()

    def getPostmanCollection(self):
        data = api.as_postman(urlvars=False, swagger=True)
        print(json.dumps(data))

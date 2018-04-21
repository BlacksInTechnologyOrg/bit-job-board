import datetime
from flask import current_app
from flask_script import Command
from flask_security.confirmable import confirm_user
from flask_application.models import FlaskDocument
from flask_application.users.models import Contract, User


class ResetDB(Command):
    """Drops all tables and recreates them"""
    def run(self, **kwargs):
        self.drop_collections()

    @staticmethod
    def drop_collections():
        for klass in FlaskDocument.all_subclasses():
            klass.drop_collection()


class PopulateDB(Command):
    """Fills in predefined data to DB"""
    def run(self, **kwargs):
        self.create_roles()
        self.create_users()
        self.create_contract()
        self.add_dubh_stuff()


    @staticmethod
    def create_roles():
        for role in ('admin', 'editor', 'author'):
            current_app.user_datastore.create_role(name=role, description=role)
        current_app.user_datastore.commit()

    @staticmethod
    def create_users():
        for u in (('matt', 'matt@lp.com', 'password', ['admin'], True),
                  ('joe', 'joe@lp.com', 'password', ['editor'], True),
                  ('jill', 'jill@lp.com', 'password', ['author'], True),
                  ('tiya', 'tiya@lp.com', 'password', [], False),
                  ('dubh3124', 'dubh3124@gmail.com', 'password', [], True),
                  ('rdugue', 'rdugue1@gmail.com', 'password', [], True)):
            user = current_app.user_datastore.create_user(
                username=u[0],
                email=u[1],
                password=u[2],
                roles=u[3],
                active=u[4]
            )
            confirm_user(user)

            current_app.user_datastore.commit()

    @staticmethod
    def create_contract():
        for title, description, author, accepted_by, status in (('Job1', 'Programmer', 'matt','dubh3124',"Completed"), ('Job2', 'SySAdmin', 'joe', 'dubh3124',"Completed"), ('Job3', 'Programmer', 'dubh3124', 'joe', "In Progress")):
            user = User.objects

            test = Contract()
            test.author = user.get(username=author).pk
            test.title = title
            test.description = description
            test.publishdate = datetime.datetime.utcnow().isoformat(' ', 'seconds')
            test.accepted_by = user.get(username=accepted_by).pk
            test.accepted_date = datetime.datetime.utcnow().isoformat(' ', 'seconds')
            test.status = status
            test.save()
    @staticmethod
    def add_dubh_stuff():
        User.objects.get(username="dubh3124").update(first_name = "Herman",last_name = "Haggerty")






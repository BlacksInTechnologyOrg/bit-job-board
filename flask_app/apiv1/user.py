import logging
from flask import Blueprint, jsonify, request
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity,
    get_csrf_token,
    current_user,
)
from flask_restplus import Api, Resource, Namespace
from ..errors import UserNotFoundError
from ..messaging import MessageHandler
from ..models.user import User

# TODO: Fix F811 flake8 errors

log = logging.getLogger(__name__)

userapi = Namespace("users", description="Authorization API")
mh = MessageHandler()


@userapi.route("/Foo")  # noqa: F811
class Users(Resource):
    @jwt_required
    def get(self):
        return {
            "message": "Hi! {USER}. This is a GET response".format(
                USER=current_user.username
            )
        }

    @jwt_required
    def post(self):
        return {"message": "Hi! {USER}".format(USER=current_user.username)}


@userapi.route("/newMessage")  # noqa: F811
class Users(Resource):
    @jwt_required
    def post(self):
        try:
            data = userapi.payload
            if User.objects(username__exact=data["recipient"]).count() != 1:
                raise UserNotFoundError
            else:
                mh.newMessage(
                    current_user, data["recipient"], data["subject"], data["message"]
                )
                return {"message": "Message Sent"}
        except UserNotFoundError as e:
            logging.error(e)
            return {"message": e.error}
        except Exception as e:
            logging.error(e, exc_info=True)
            return {"message": "Oops!"}


@userapi.route("/getMessage")  # noqa: F811
class Users(Resource):
    @jwt_required
    def get(self):
        try:
            allmessages = mh.getAllMessages(
                current_user.username, request.args["pgnum"]
            )
            return {"messages": allmessages}
        except Exception as e:
            log.error(e, exc_info=True)
            return {"message": "Oops!"}


@userapi.route("/deleteMessage")  # noqa: F811
class Users(Resource):
    @jwt_required
    def delete(self):
        try:
            mh.deleteMessage("5b4c3feaf4da5d71b84d8642")
        except Exception as e:
            log.error(e, exc_info=True)
            return {"message": "Oops!"}

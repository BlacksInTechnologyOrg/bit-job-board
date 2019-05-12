import logging
from mongoengine.errors import DoesNotExist, NotUniqueError
from flask import jsonify, Response
from flask_restplus import Resource, Namespace, fields
from ..models.user import User
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
    set_access_cookies,
    set_refresh_cookies,
    unset_jwt_cookies,
    jwt_refresh_token_required,
)

jwt = JWTManager()

authapi = Namespace("auth", description="Authorization API")

creds = authapi.model(
    "Credentials",
    {
        "username": fields.String(required=True, description="Username"),
        "password": fields.String(required=True, description="Password"),
    },
)

user = User()


@jwt.user_loader_callback_loader
def user_loader_callback(identity):
    if not User.objects(username__exact=identity):
        return None

    return User.objects(username__exact=identity).get()


@jwt.user_loader_error_loader
def custom_user_loader_error(identity):
    ret = {"msg": "User {} not found".format(identity)}
    return jsonify(ret), 404


@authapi.route("/registration")
# @api.doc(False)
class UserRegistration(Resource):
    @authapi.expect(creds)
    def post(self):
        data = authapi.payload

        try:
            user.username = data["username"]
            user.email = data["email"]
            user.firstname = data["firstname"]
            user.lastname = data["lastname"]
            user.password = user.generate_hash(data["password"])
            user.save()

            access_token = create_access_token(identity=data["username"])
            refresh_token = create_refresh_token(identity=data["username"])

            resp = jsonify({"message": f'User {data["username"]} was created'})

            set_access_cookies(resp, access_token)
            set_refresh_cookies(resp, refresh_token)

            return resp
        except NotUniqueError as e:
            logging.exception(e)
            resp = jsonify({"message": "Username already exists!"})
            resp.status_code = 422
            return resp
        except Exception:
            logging.exception(Exception)
            resp = jsonify({"message": "Something went wrong!"})
            resp.status_code = 500


@authapi.route("/login")
class UserLogin(Resource):
    @authapi.expect(creds)
    def post(self):
        try:
            logging.info("Logging In")
            data = authapi.payload
            current_user = User.objects.get(username=data["username"])
            if user.verify_hash(data["password"], current_user.password):
                access_token = create_access_token(identity=data["username"])
                refresh_token = create_refresh_token(identity=data["username"])

                resp = jsonify(
                    {"message": "Logged in as {}".format(current_user.username)}
                )

                set_access_cookies(resp, access_token)
                set_refresh_cookies(resp, refresh_token)
                return resp
            else:
                response = jsonify({"message": "Wrong username or password!"})
                response.status_code = 401
                return response
        except DoesNotExist:
            response = jsonify({"message": "Wrong username or password!"})
            response.status_code = 401
            return response
        except Exception:
            logging.exception("Oops", exc_info=True)
            response = jsonify({"message": "Somthing Went Wrong!"})
            response.status_code = 500
            return response


@authapi.route("/logout")
class UserLogout(Resource):
    def post(self):
        try:
            resp = jsonify({"logout": True})
            unset_jwt_cookies(resp)
            return resp
        except Exception:
            logging.exception("Token not deleted after log out")
            resp = jsonify({"error": "Something went wrong!"})
            unset_jwt_cookies(resp)
            return resp


@authapi.route("/token/refresh")
class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        try:
            current_user = get_jwt_identity()
            access_token = create_access_token(identity=current_user)
            resp = jsonify({"message": "Token Refreshed!"})
            set_access_cookies(resp, access_token)
            return resp
        except Exception:
            logging.exception("Token could not be refreshed")
            return jsonify({"error": "Something went wrong!"})

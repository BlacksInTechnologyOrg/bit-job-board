from flask import Blueprint
from flask_restplus import Api
from ..apiv1.user import userapi
from ..apiv1.auth import authapi
from ..apiv1.job import jobapi
from ..apiv1.contract import contractapi


api1 = Blueprint("api1", __name__, url_prefix="/api")
api = Api(
    api1, title="BIT Job Board", version="1.0", description="BIT Job Board Api Server"
)

api.add_namespace(authapi)
api.add_namespace(userapi)
api.add_namespace(jobapi)
api.add_namespace(contractapi)

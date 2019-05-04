from flask import Flask, render_template
import os
from flask_app.config import config

FRONTEND_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "front-end")
)
if not os.path.exists(FRONTEND_DIR):
    raise Exception("Client App directory not found: {}".format(FRONTEND_DIR))


def create_app(config_name):
    # W605 invalid escape sequence. Seems to be a new flake8 warning that Flask has to fix.
    app = Flask(  # noqa: W605
        __name__,
        static_folder=os.path.join(FRONTEND_DIR, "dist", "static"),
        template_folder=os.path.join(FRONTEND_DIR, "dist"),
    )
    app.config.from_object(config[config_name])
    app.logger.info("Config: %s" % config_name)

    #  Logging
    import logging

    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(levelname)s: %(message)s " "[in %(pathname)s:%(lineno)d]",
        datefmt="%Y%m%d-%H:%M%p",
    )

    from flask_app.apiv1.auth import jwt

    jwt.init_app(app)

    # CORS
    from flask_cors import CORS

    CORS(app, resources={r"/api/*": {"origins": "*"}}, supports_credentials=True)

    # Email
    from flask_mail import Mail

    app.mail = Mail(app)

    # MongoEngine
    from flask_app.db_init import db

    app.db = db
    app.db.init_app(app)

    # Elasticsearch
    from elasticsearch_dsl import connections

    connections.create_connection(
        alias="bonsai", hosts=[os.getenv("ELASTICSEARCH_URL")], timeout=60
    )

    # Business Logic
    # http://flask.pocoo.org/docs/patterns/packages/
    # http://flask.pocoo.org/docs/blueprints/
    from flask_app.apiv1 import api1

    app.register_blueprint(api1)

    # from flask_app.script import resetdb, populatedb
    # # Click Commands
    # app.cli
    # app.cli.add_command(resetdb)
    # app.cli.add_command(populatedb)

    @app.route("/", defaults={"path": ""})
    @app.route("/<path:path>")
    def catch_all(path):
        return render_template("index.html")

    return app

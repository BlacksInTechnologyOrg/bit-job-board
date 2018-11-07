import os
from flask_app import create_app, script

app = create_app(os.getenv("FLASK_ENV").lower())
script.register(app)

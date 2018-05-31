import logging
import os

class Config(object):
    def __init__(self):
        self.DEBUG = False
        self.TESTING = False
        self.HEROKU = False
        self.PRODUCTION = False

        self.SECRET_KEY = '{SECRET_KEY}'
        self.SITE_NAME = 'Flask Site'
        self.LOG_LEVEL = logging.DEBUG
        self.SERVER_NAME = 'localhost:5000'

        self.SYS_ADMINS = ['foo@example.com']
        self.ASSETS_DEBUG = True

        # Mongodb support
        # Uncomment and fill out for shared DB connection
        self.MONGODB_SETTINGS = self.dbLocation("cloud", username="", password="", db_name="")

        # Uncomment and fill out for custom DB coonnection
        # self.MONGODB_SETTINGS = self.dbLocation("local", db_conn="")

        # Configured for Gmail
        self.DEFAULT_MAIL_SENDER = 'Admin < username@example.com >'
        self.MAIL_SERVER = 'smtp.gmail.com'
        self.MAIL_PORT = 465
        self.MAIL_USE_SSL = True
        self.MAIL_USERNAME = 'EMAIL'
        self.MAIL_PASSWORD = 'PASSWORD'

        # Flask-Security setup
        self.SECURITY_EMAIL_SENDER = 'Security < security@example.com >'
        self.SECURITY_LOGIN_WITHOUT_CONFIRMATION = True
        self.SECURITY_REGISTERABLE = True
        self.SECURITY_RECOVERABLE = True
        self.SECURITY_URL_PREFIX = '/auth'
        self.SECURITY_POST_LOGIN_VIEW = '/profile'
        self.SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'
        # import uuid; salt = uuid.uuid4().hex
        self.SECURITY_PASSWORD_SALT = '2b8b74efc58e489e879810905b6b6d4dc6'

        self.SECURITY_CONFIRMABLE = True
        self.SECURITY_LOGIN_WITHOUT_CONFIRMATION = False

        # CACHE
        self.CACHE_TYPE = 'simple'

    def dbLocation(self, location, db_conn=None, username=None, password=None, db_name=None):
        if location == "custom":
            uri = db_conn
            return self.mongo_from_uri(uri)
        elif location == "cloud":
            uri = "mongodb://{username}:{password}@bitjobboard-shard-00-00-dyzis.mongodb.net:27017,bitjobboard-shard-00-01-dyzis.mongodb.net:27017,bitjobboard-shard-00-02-dyzis.mongodb.net:27017/{db_name}?ssl=true&replicaSet=bitjobboard-shard-0&authSource=admin&retryWrites=true" \
                .format(username=username, password=password, db_name=db_name)
            return self.mongo_from_uri(uri)
        else:
            raise ValueError('Location must be "custom" or "cloud"')


    @staticmethod
    def mongo_from_uri(uri):
        conn_settings = {
            'host': uri
        }
        return conn_settings


class ProductionConfig(Config):
    def __init__(self):
        super(ProductionConfig, self).__init__()
        self.ENVIRONMENT = 'Production'
        self.HEROKU = True
        self.PRODUCTION = True
        self.LOG_LEVEL = logging.INFO
        self.SERVER_NAME = 'bitregistry-dev.herokuapp.com'

        self.MAIL_SERVER = 'smtp.mandrillapp.com'
        self.MAIL_PORT = 465
        self.MAIL_USE_SSL = True
        self.MAIL_USERNAME = os.getenv('MANDRILL_USERNAME')
        self.MAIL_PASSWORD = os.getenv('MANDRILL_APIKEY')

        self.MONGODB_SETTINGS = self.mongo_from_uri('mongodb://bitregistry-user:BIT123@ds111648.mlab.com:11648/heroku_xc23j00v')


class DevelopmentConfig(Config):
    '''
    Use "if app.debug" anywhere in your code,
    that code will run in development mode.
    '''
    def __init__(self):
        super(DevelopmentConfig, self).__init__()
        self.ENVIRONMENT = 'Dev'
        self.DEBUG = True
        self.TESTING = False


class TestingConfig(Config):
    '''
    A Config to use when we are running tests.
    '''
    def __init__(self):
        super(TestingConfig, self).__init__()
        self.ENVIRONMENT = 'Testing'
        self.DEBUG = False
        self.TESTING = True

        self.MONGODB_SETTINGS = self.mongo_from_uri(
            'mongodb://localhost:27017/testing'
        )


environment = os.getenv('ENVIRONMENT', 'DEVELELOPMENT').lower()
# Alternatively this may be easier if you are managing multiple aws servers:
# environment = socket.gethostname().lower()

if environment == 'testing':
    app_config = TestingConfig()
elif environment == 'production':
    app_config = ProductionConfig()
else:
    app_config = DevelopmentConfig()

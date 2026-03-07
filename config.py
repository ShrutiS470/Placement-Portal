class localdev:
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'sqlite:///placements.sqlite3'
    SECRET_KEY = 'shhhh its a secret'
    SECURITY_TRACKABLE = True
    SECURITY_TOKEN_AUTHENTICATION_HEADER = 'Authorization'

class prod:
    DEBUG = False

    SQLALCHEMY_DATABASE_URI = 'sqlite:///placements.sqlite3'
    #SECRET_KEY = 'env.get("SECRET_KEY")'
    SECURITY_TRACKABLE = True
    SECURITY_TOKEN_AUTHENTICATION_HEADER = 'Authorization'
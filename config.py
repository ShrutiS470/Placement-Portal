class localdev:
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'sqlite:///placements.sqlite3'
    SECRET_KEY = 'shhhh its a secret'
    SECURITY_TRACKABLE = True
    SECURITY_TOKEN_AUTHENTICATION_HEADER = 'Authorization'

    MAIL = 'localhost'
    MAIL_PORT = 1025
    MAIL_DEFAULT_SENDER = 'donot-reply@abc.com'

    CACHE_TYPE = 'RedisCache'
    CACHE_REDIS_URL = 'redis://localhost:6379/3'
    CACHE_DEFAULT_TIMEOUT = 30

class prod:
    DEBUG = False

    SQLALCHEMY_DATABASE_URI = 'sqlite:///placements.sqlite3'
    #SECRET_KEY = 'env.get("SECRET_KEY")'
    SECURITY_TRACKABLE = True
    SECURITY_TOKEN_AUTHENTICATION_HEADER = 'Authorization'

class celeryConfig:
    broker_url = 'redis://localhost:6379/1'
    result_backend = 'redis://localhost:6379/2'
    timezone = 'Asia/Kolkata'
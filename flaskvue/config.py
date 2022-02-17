from datetime import timedelta

class Config:
    SECRET_KEY = 'secret'

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'
    API_TITLE = "My API"
    API_VERSION = "v1"
    OPENAPI_VERSION = "3.0.2"

    JWT_SECRET_KEY = "super-secret"
    JWT_TOKEN_LOCATION = ["headers","cookies"]
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(seconds=3600)
    JWT_COOKIE_SECURE = False
    JWT_REFRESH_TOKEN_EXPIRES= timedelta(days=30)
    JWT_COOKIE_CSRF_PROTECT = False
    CORS_SUPPORTS_CREDENTIALS = True
    


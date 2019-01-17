"""Default configuration

Use env var to override
"""
import datetime

DEBUG = True
SECRET_KEY = "changeme"

SQLALCHEMY_DATABASE_URI = "sqlite:///D:/whatever.db"
SQLALCHEMY_TRACK_MODIFICATIONS = False

JWT_BLACKLIST_ENABLED = True
JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']

JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(minutes=30)

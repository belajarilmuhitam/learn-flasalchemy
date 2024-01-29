import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    HOST = os.environ.get("DB_HOST")
    PORT = os.environ.get("DB_PORT", "3306")
    DATABASE = os.environ.get("DB_DATABASE")
    USERNAME = os.environ.get("DB_USERNAME")
    PASSWORD = os.environ.get("DB_PASSWORD")

    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}?charset=utf8mb4"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True

import os

class Config:
    DEBUG = True
    TESTING = False
    SECRET_KEY = 'e93b50c764e469b9c8aab5ad28a93'
    HOST = '127.0.0.1'
    PORT = 5000

  
    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'instance', 'app.db')

    SQLALCHEMY_TRACK_MODIFICATIONS = False

class Config:
    DEBUG = True
    TESTING = False
    SECRET_KEY = 'e93b50c764e469b9c8aab5ad28a93'
    HOST = '127.0.0.1'
    PORT = 5000
    
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://postgres@db:5432/flask_db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
class DevelopmentConfig(Config):
    DEBUG = True
    
class TestingConfig(Config):
    TESTING = True
    DEBUG = True
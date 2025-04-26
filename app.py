from flask import Flask
from alunos.alunos_routes import alunos_routes
from professores.professores_routes import professores_routes
from turmas.turmas_routes import turmas_routes
from reset_routes import reset_routes
from home_routes import home_routes
from config import Config
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    
   
    app.register_blueprint(home_routes)
    app.register_blueprint(alunos_routes)
    app.register_blueprint(professores_routes)
    app.register_blueprint(turmas_routes)
    app.register_blueprint(reset_routes)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
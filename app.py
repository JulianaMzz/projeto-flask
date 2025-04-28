from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from swagger.swagger_config import api
from swagger.namespace.alunos_namespace import alunos_ns
from swagger.namespace.professores_namespace import professores_ns
from swagger.namespace.turma_namespace import turmas_ns




from reset_routes import reset_routes
from home_routes import home_routes


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
 
    db.init_app(app)

   
    api.init_app(app)

   
    api.add_namespace(alunos_ns, path='/alunos')
    api.add_namespace(professores_ns, path='/professores')
    api.add_namespace(turmas_ns, path='/turmas')

  
    app.register_blueprint(home_routes)
    app.register_blueprint(reset_routes)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)

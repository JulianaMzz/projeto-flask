from flask import Blueprint

home_routes = Blueprint('home_routes', __name__)
 
@home_routes.route('/')
def home():
     return "Bem-vindo à API escolar"
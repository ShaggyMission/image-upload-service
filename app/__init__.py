from flask import Flask
from flasgger import Swagger
from .config import load_env_vars
from .routes.image_routes import image_bp

def create_app():
    load_env_vars()

    app = Flask(__name__)
    Swagger(app, template_file='docs/swagger.yml')  

    app.register_blueprint(image_bp, url_prefix='/pets/images')

    return app

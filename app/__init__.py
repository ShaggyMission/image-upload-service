from flask import Flask
from flasgger import Swagger
from flask_cors import CORS 
from .config import load_env_vars
from .routes.image_routes import image_bp

def create_app():
    load_env_vars()

    app = Flask(__name__)
    CORS(app)
    
    Swagger(app,
            template_file='docs/swagger.yml',
            config={
                "specs": [
                    {
                        "endpoint": 'apispec_1',
                        "route": '/pets/imagesUpload-docs.json',
                        "rule_filter": lambda rule: True,   
                        "model_filter": lambda tag: True,     
                    }
                ],
                "specs_route": "/pets/imagesUpload-docs",
                "headers": []
            })

    app.register_blueprint(image_bp, url_prefix='/pets/images')

    return app

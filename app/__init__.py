from flask import Flask, render_template, request, redirect, Blueprint, url_for
from dotenv import load_dotenv
import os

###################
### APPLICATION ###
###################
def create_app():
    load_dotenv()
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY = os.getenv('key'),
        DATABASE = os.path.join(app.instance_path, os.getenv('db'))
    )
    if not os.path.exists(app.instance_path):
        os.makedirs(app.instance_path)
    from . import db
    db.init_app(app)
    
    from .authviews import authviews
    from .views import views
    app.register_blueprint(authviews, url_prefix='/auth')
    app.register_blueprint(views, url_prefix='/')
        
    return app


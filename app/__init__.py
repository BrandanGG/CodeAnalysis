from flask import Flask, render_template, request, redirect, Blueprint, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Length
import bcrypt
import secrets
import os


#######################
### FORM MANAGEMENT ###
#######################

# form for users to sign in on home page
class loginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=10, max=40)])
    password = StringField('Password', validators=[InputRequired(), Length(min=10, max=40)])
    submit = SubmitField('Submit')

class registerForm(loginForm):
    email = StringField('email', validators=[InputRequired(), Length(min=4, max=40)])

########################
### Password Hashing ###
########################

def hash_pw(password:str) -> str:
    return bcrypt.hashpw(password.encode('utf-8', bcrypt.gensalt(rounds=15)))

def check_pw(password:str, stored_hash:str) -> bool:
    return bcrypt.check_pw(password.encode('utf-8'), stored_hash)


###################
### APPLICATION ###
###################
def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY = secrets.token_hex(32),
        DATABASE = os.path.join(app.instance_path, 'data_storage.sqlite')
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


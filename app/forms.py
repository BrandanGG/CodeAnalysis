from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Length
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

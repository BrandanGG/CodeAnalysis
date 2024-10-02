from flask import Blueprint, render_template, redirect, url_for, session, request
from . import loginForm, registerForm

authviews = Blueprint('authviews', __name__)


# needs login logic to be built out. First need to set up SQL Lite and account registration, and finalize the HTML and CSS
@authviews.route('/login', methods=['GET', 'POST'])
def login():
    form = loginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            # Process login logic
            return f'You have successfully logged in as {username}'
        else:
            # Handle form validation errors (optional)
            pass
    return render_template('login.html', form = loginForm())


@authviews.route('/register', methods=['GET', 'POST'])
def register():
    form = registerForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data # add logic for check_pw and pulling the right hash from the DB once its set up
            email = form.email.data
            # Process login logic
            return f'You have successfully registered as {username}'
        else:
            # Handle form validation errors (optional)
            pass
    return render_template('register.html', form = registerForm())

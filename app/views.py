from flask import Blueprint, redirect, url_for, request

views = Blueprint('views', __name__)

# Add this route to redirect from the root ("/") to "/auth/login" eventually move to a standard views.py file
@views.route('/', methods=['GET'])
def root():
    return redirect(url_for('authviews.login'))

@views.route('/dashboard', methods=['GET'])
def dashboard():
    return 'You have successfully logged in'
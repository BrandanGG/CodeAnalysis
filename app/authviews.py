from flask import Blueprint, render_template, redirect, url_for, session, request, g, flash, get_flashed_messages
from .forms import loginForm, registerForm
from .db import get_db
from .encryption import hash_pw, check_pw
authviews = Blueprint('authviews', __name__)

# will be storing both email and password in an encrypted state.


# needs login logic to be built out. First need to set up SQL Lite and account registration, and finalize the HTML and CSS
@authviews.route('/login', methods=['GET', 'POST'])
def login():
    form = loginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
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
            # Take in form submissions
            username = form.username.data
            password = hash_pw(form.password.data)
            email = form.email.data

            # Check if username or email already exists
            if doesUNameExist(username):
                flash('Username already exists.', 'error')
            if doesEmailExist(email):
                flash('Email already exists.', 'error')

            # Validate other fields
            for field, value in [('Username', username), ('Password', password), ('Email', email)]:
                if not value:
                    flash(f'{field} is required.', 'error')

            # If no errors, insert into the database
            if not get_flashed_messages(category_filter=['error']):  # No errors flashed
                try:
                    db = get_db()
                    db.execute(
                        'INSERT INTO users (username, password, email) VALUES (?, ?, ?)', 
                        (username, password, email)
                    )
                    db.commit()
                    flash('Registration successful!', 'success')
                    return redirect(url_for('views.root')) # send to root, which redirects to login
                except db.IntegrityError:
                    flash('An error occurred while saving the user.', 'error')
        else:
            # Handle form validation errors (optional)
            pass
    return render_template('register.html', form = form)

#check for existing users during registration
def doesUNameExist(username: str) -> bool:
    db = get_db()
    cur = db.execute('SELECT * FROM users WHERE username=?', (username,))
    return cur.fetchone() is not None
def doesEmailExist(email: str) -> bool:
    db = get_db()
    cur = db.execute('SELECT * FROM users WHERE email=?', (email,))
    return cur.fetchone() is not None

from flask import Blueprint, render_template, redirect, url_for, session, request, g, flash, get_flashed_messages
from .forms import loginForm, registerForm
from .db import get_db
from .encryption import hash_pw, check_pw

authviews = Blueprint('authviews', __name__)

# needs login logic to be built out. First need to set up SQL Lite and account registration, and finalize the HTML and CSS
@authviews.route('/login', methods=['GET', 'POST'])
def login():
    form = loginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            #Collect form data
            username = form.username.data
            password = form.password.data
            # checking if the username exists in the database, and if the password is correct to the stored database.
            if not doesUNameExist(username) or not isPasswordCorrect(username, password):
                print('error with username or password')
                flash('Invalid Username or Password.', 'error')
                return render_template('login.html', form = form)
            else: # if the submissions were correct, log the user into the dashboard
                print('username is correct')
                return redirect(url_for('views.dashboard')) 
        else:
            # Handle form validation errors (optional)
            flash('Error processing your request.', 'error')
    return render_template('login.html', form = form)


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
                return render_template('register.html', form=form, username = username, email = email)
            if doesEmailExist(email):
                flash('Email already exists.', 'error')
                return render_template('register.html',form=form, username = username, email = email)

            # Validate other fields
            for field, value in [('Username', username), ('Password', password), ('Email', email)]:
                if not value:
                    flash(f'{field} is required.', 'error')
                    return render_template('register.html',form=form, username = username, email = email)


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
#check for existing email addresses during registration
def doesEmailExist(email: str) -> bool:
    db = get_db()
    cur = db.execute('SELECT * FROM users WHERE email=?', (email,))
    return cur.fetchone() is not None
#check if password stored is == password submitted during login
def isPasswordCorrect(username: str, password: str) -> bool:
    db = get_db()
    cur = db.execute('SELECT password FROM users WHERE username=?', (username,))
    result = cur.fetchone()

    if result is None:
        print(f"No user found for username: {username}")
        return False
    
    stored_hash = result[0]
    
    if check_pw(password, stored_hash):
        return True
    else:
        print(f"Password comparison failed for user: {username}")
        return False

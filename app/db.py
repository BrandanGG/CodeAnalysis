import sqlite3
import click
from flask import current_app, g 

# g is a special object that is unique for each request. It is used to store data that might be accessed by multiple functions during the request. 
# The connection is stored and reused instead of creating a new connection if get_db is called a second time in the same request.
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db

# close DB connection
def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

# used to open the initialize the DB.        
def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

#CLI that calls the init_db() and shows a success message
@click.command('init-db')
def init_db_command():
    #Clear the existing data and create new tables.
    init_db()
    click.echo('Initialized the database.')
    

# used to register the functions with the application... imported into __init__.py
def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
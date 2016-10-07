"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request, session, url_for, abort, make_response, json
from itsdangerous import *
from QUASAR import app
from flaskext.mysql import MySQL
from QUASAR.models.user import User

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'general/index.html',
        title='Home Page'
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'general/contact.html',
        title='Contact',
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'general/about.html',
        title='About',
        message='Your application description page.'
    )


@app.route('/auth/register', methods=['POST'])
def register_user():

    username = request.form['user_name']
    email = request.form['email']
    password = request.form['password']

    if request.method == 'POST':
        user = User(username, "None", "None", email, "None", password, 1, 1, None, None, None, None,None, None)
       
        return json.dumps({'html':'<span>Nice</span>'})
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'})




"""
The flask application package.
"""

from flask import Flask, render_template, request, session, url_for, abort, make_response, json
from itsdangerous import *
from QUASAR.common.database import * 
from flaskext.mysql import MySQL

app = Flask(__name__)

SECRET_KEY = 'you-will-never-guess'
mysql = MySQL()
app.config.from_pyfile('common/database.py')
mysql.init_app(app)    
conn = mysql.connect()
cursor = conn.cursor()
#cursor.execute("INSERT INTO user (user_name, first_name, last_name, email, password) VALUES ('new_person1', 'Maxix',  'Minix', 'minmaxxkemar.com', 'nikki')")
data = cursor.fetchone()
print(data)
conn.commit() 



import QUASAR.views


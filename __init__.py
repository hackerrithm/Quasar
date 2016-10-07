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

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'kemar'
app.config['MYSQL_DATABASE_DB'] = 'quasardb'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)
    
conn = mysql.connect()
cursor = conn.cursor()
#cursor.execute("INSERT INTO user (user_name, first_name, last_name, email, password) VALUES ('GALLOWAY', 'Maxix',  'Minix', 'minmaxxkemar.com', 'nikki')")
data = cursor.fetchone()
print(data)
conn.commit() 




import QUASAR.views


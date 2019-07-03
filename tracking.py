#Code from https://realpython.com/python-web-applications-with-flask-part-i/
from os.path import abspath, dirname, join
from flask import flash, Flask, Markup, redirect, render_template, url_for
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf import Form
from wtforms import fields
from wtforms.ext.sqlalchemy.fields import QuerySelectField

_cwd = dirname(abspath(__file__))

SECRET_KEY = 'flask-session-insecure-secret-key' #sign Flask’s sessions,
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + join(_cwd, 'flask-tracking.db') #point to sqlite db file
SQLALCHEMY_ECHO = True
WTF_CSRF_SECRET_KEY = 'this-is-not-random-but-it-should-be'  #sign WTForms’ CSRF tokens.


app = Flask(__name__)
app.config.from_object(__name__)

db = SQLAlchemy(app)
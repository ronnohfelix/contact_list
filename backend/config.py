from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS # remove cors error while fetching data from frontend

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' # database path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # no modification tracking

db = SQLAlchemy(app) # database object
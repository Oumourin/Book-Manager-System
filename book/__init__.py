from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# creating flask instance
app = Flask(__name__)

# load configuration
app.config.from_object('configuration')

# handling database
db = SQLAlchemy(app)

# mount controllers
from . import controller

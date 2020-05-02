from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)

# Load config
app.config.from_object(Config)

# Load database
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Load login manager
login = LoginManager(app)
login.login_view = 'login'

from app import routes, models
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager  = LoginManager(app)
bcrypt = Bcrypt(app)

app.config['SECRET_KEY'] = '123QWE'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'


from post import views
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.config['SECRET_KEY'] = '123QWE'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'


from post import views
from flask import render_template, url_for
from .forms import *
from post import app

posts = [
    {
        'author': 'Student',
        'title': 'Flask',
        'content': 'Flask deployment',
        'date': 'May 5, 2022',
    },
    {
        'author': 'Student 2',
        'title': 'Flask',
        'content': 'Flask deployment',
        'date': 'May 5, 2022',
    },
    {
        'author': 'Student 3',
        'title': 'Flask',
        'content': 'Flask deployment',
        'date': 'May 5, 2022',
    },

]

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html', posts=posts)

@app.route("/profile")
def profile():
    return render_template('profile.html', title="User Profile")

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title="Register", form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title="login", form=form)
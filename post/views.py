from flask import redirect, render_template, url_for, flash
from .forms import *
from .models import *
from post import app, bcrypt
from flask_login import login_user, current_user, logout_user


@app.route("/")
@app.route("/home")
def home():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)

@app.route("/profile")
def profile():
    return render_template('profile.html', title="User Profile")

@app.route("/new/post", methods=['GET', 'POST'])
def create():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        
        flash('Post created Successfully', 'success')
        return redirect(url_for('home'))
    return render_template('create.html', title="New Post", form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        pw_hash = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=pw_hash)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        
        flash('Your account has been created successfully', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title="Register", form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)        
            flash('Login successful', 'success')
            return redirect(url_for('home'))
    
    return render_template('login.html', title="login", form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))
    

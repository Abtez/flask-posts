from fileinput import filename
import secrets
import os
from flask import redirect, render_template, request, url_for, flash
from .forms import *
from .models import *
from post import app, bcrypt
from flask_login import login_user, current_user, logout_user


@app.route("/")
@app.route("/home")
def home():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)

def save_avatar(form_avatar):
    random_hex = secrets.token_hex(8)
    _, file_ext = os.path.splitext(form_avatar.filename)
    avatar_fn = random_hex + file_ext
    avatar_path = os.path.join(app.root_path, 'static/img', avatar_fn)
    form_avatar.save(avatar_path)
    return avatar_fn

@app.route("/profile", methods=['GET', 'POST'])
def profile():
    form = UpdateProfileForm()
    if form.validate_on_submit():
        if form.avatar.data:
            avatar_file = save_avatar(form.avatar.data)
            current_user.avatar = avatar_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Account info has been updated', 'success')
        return redirect(url_for('profile'))
    
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    
    avatar = url_for('static', filename=f'img/{current_user.avatar}')
    return render_template('profile.html', title="User Profile", form=form, avatar=avatar)

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
    

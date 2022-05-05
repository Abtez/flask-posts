from turtle import title
from flask import Flask, render_template, url_for

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)
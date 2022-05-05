from flask import Flask, render_template

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
]

@app.route("/")
def hello_world():
    return render_template('index.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)
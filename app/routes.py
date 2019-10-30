from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Roy'}
    posts = [
        {
            'author': {'username': 'Dragan'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Yolanda'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

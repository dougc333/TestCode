from flask import render_template
from hellotemplates1 import app


@app.route('/')
@app.route('/index')
def index():
	user = {'nickname':'nickname1'}
	posts = [  # fake array of posts
        { 
            'author': {'nickname': 'John'}, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': {'nickname': 'Susan'}, 
            'body': 'The Avengers movie was so cool!' 
        }
    	]
	return render_template('index.html', title='Home', user=user,posts=posts)

@app.route('/column')
def content():
	return render_template('column.html',title='Content')

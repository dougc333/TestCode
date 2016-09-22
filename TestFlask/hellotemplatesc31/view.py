from hellotemplatesc31 import app
from flask import render_template

@app.route('/index')
@app.route('/')
def index():
	return render_template('index.html')


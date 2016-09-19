from flask import render_template,redirect, flash
from helloforms import app
from .forms import LoginForm


@app.route('/index')
def index():
	print 'calling index'
	user = {'nickname':'nickname1'}
	posts = [
	{'author':{'nickname':'a'},'post':'user1 first post'},
	{'author':{'nickname':'b'},'post':'user2 first post'},
	{'author':{'nickname':'c'},'post':'user3 first post'}]
	return render_template('index.html')


@app.route('/login')
def login():
	form=LoginForm(csrf_enabled=False)
	if form.validate_on_submit():
		flash("openid='%s', remember_me='%s' ",(form.openid.data, str(form.remember_me.data)))
		return redirect('index.html')
	return render_template('login.html',title="login", form=form, providers=app.config['OPENID_PROVIDERS'])

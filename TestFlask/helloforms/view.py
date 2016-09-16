from flask import render_template,redirect, flash
from helloforms import app
from .forms import LoginForm


@app.route('/index')
def index():
	print 'calling index'
	return render_template('index.html')


@app.route('/login')
def login():
	form=LoginForm(csrf_enabled=False)
	if form.validate_on_submit():
		flash("openid='%s', remember_me='%s' ",(form.openid.data, str(form.remember_me.data)))
		return redirect('index.html')
	return render_template('login.html',title="login", form=form, providers=app.config['OPENID_PROVIDERS'])

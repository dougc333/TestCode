from flask import render_template, redirect, flash
from app import app
from .forms import LoginForm


@app.route('/login', methods=['GET','POST'])
def login():
	form = LoginForm()
	if from.validate_on_submit():
 		flash('Login requested for openid:"%s", remember_me="%s"' %
		(form.openid.data, str(form.remember_me.data)))
		return redirect('/index')
	return render_template('login.html', title='SignIn', form=form)



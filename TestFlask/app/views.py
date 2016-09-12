from app import app
from flask import render_template, flash, redirect
from .forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
  user = {'nickname': 'Aaaa'} 
  return render_template('index.html', title='Home', user=user)


@app.route('/login', methods=['GET','POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    flash('login requeseted for openid="%s" rembmber_me="%s" % ()' %
          (form.openid.data,str(form.remember_me.data)))
    return redirect('/index')
  return render_template('login.html', title='Login.html', form=form,
                         providers=app.config['OPENID_PROVIDERS'])



@app.route('/user')
def user():
  return render_template('user.html', title="User")
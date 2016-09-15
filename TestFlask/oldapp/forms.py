from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtfforms.validators import DataRequired

class LoginForm(Form):
	openid = StringField('openid', validator=[DataRequired()])
	remember_me = BooleanField('remember_me',default=False)

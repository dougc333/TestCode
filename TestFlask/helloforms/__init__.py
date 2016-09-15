from flask import Flask

app = Flask('__name__', root_path='/Users/dc/TestCode/TestFlask/helloforms')
app.config.from_pyfile('config.py')
from helloforms import view

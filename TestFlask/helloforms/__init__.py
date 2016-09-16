from flask import Flask

app = Flask('__name__', root_path='helloforms')
app.config.from_pyfile('config.py')
from helloforms import view

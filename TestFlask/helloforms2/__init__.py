from flask import Flask



app = Flask('__name__', root_path='helloforms2')
print 'before loading config'
app.config.from_pyfile('config.py')
print 'after loadign config and before importing view'
from helloforms2 import view
print 'view imported'

#!/Users/dc/TestCode/TestFlask/Flask/bin/python


from flask import Flask
from flask import render_template
from flask import send_file


app = Flask(__name__)

@app.route('/')
def index():
  print 'function index()'
  return send_file('templates/index.html')

@app.route('/simple')
def simple():
   print 'function simple()'
   return send_file('templates/simpleindex.html')

if __name__ == '__main__':
  app.run('0.0.0.0')

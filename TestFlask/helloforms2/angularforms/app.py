#!/Users/dc/TestCode/TestFlask/flask/bin/python

from flask import Flask
from flask import render_template
from flask import send_file

app = Flask(__name__)


@app.route('/')
def index():
  return send_file('templates/index.html')

@app.route('/test')
def test():
   return 'asdfasfas....test....'

if __name__ == "__main__":
  app.run(host='0.0.0.0')



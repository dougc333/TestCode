import flask


app = flask.Flask(__name__)
#test with gunicorn. remove app.run
app.run(debug=True)

from flask import Flask


app = Flask("__name__")
#app.run(debug=True)


@app.route('/')
def index():
	return "asdfaasfdasdfa"


app.run(debug=True)


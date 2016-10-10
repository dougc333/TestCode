from flask import Flask
from flask_sockets import Sockets



app=Flask("__name__")
sockets = Sockets(app)


@sockets.route('/echo')
def es(ws):
	while True:
		ws.send('hello socket here i am')

@app.route('/normal')
def n():
	return "hello app here i am"






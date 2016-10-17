from flask import Flask
from flask_socketio import SocketIO



app=Flask(__name__)
sockets = SocketIO(app)
if __name__ == "__main__":
	sockets.run(app)

@sockets.route('/echo')
def es(ws):
	while True:
		ws.send('hello socket here i am')

@app.route('/normal')
def n():
	return "hello app here i am"






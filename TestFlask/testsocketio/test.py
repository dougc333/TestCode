from flask import Flask
from flask_socketio import SocketIO
from flask import render_template
from flask import session
from flask_socketio import join_room
from flask_socketio import leave_room
from flask_socketio import emit
import os
from os import path

app = Flask(__name__,root_path='testsocketio')
#app.config['SECRET_KEY'] = 'asdf'
#app.debug='debug'
sockets = SocketIO(app)
#sockets.init_app(app)

#if __name__ == "__main__":
	#app = Flask(__name__,root_path='testsocketio')
	#print "app run"
	##app.run(debug=True)
#	sockets.run(app)


@app.route('/')
def r():
	return 'this is app.route for /'

@app.route('/test', methods=['GET','POST'])
def a():
	print 'function a, render template for test.html'
	print 'app.root_path:' , app.root_path
	print 'should have seen path!!!'
	return render_template('test.html')


@sockets.on('message')
def handle_message(message):
	print 'socketio handle_message'
	print "socketio received message:", message

@sockets.on('json')
def handle_json(message):
	print "handle_json:", message

@sockets.on('event')
def handle_event(custom_event):
	print "custom event:", custom_event


@sockets.on('joined', namespace='/chat')
def joined(message):
	""" join
 	"""
	print 'socketio joined'
	room = session.get('room')
	join_room(room)
	semit('status', {'msg': session.get() + ''}, room=room)

@sockets.on('text', namespace='/chat')
def text(message, namespace='/chat'):
	""" sent by client
	"""
	print 'socketio text'
	room = session.get('room')
	emit('message', {'msg':session.get('name')+':'+ message['msg']}, room='room')


@sockets.on('left', namespace='/chat')
def left(message):
	"""
	"""
	print 'socketio left'
	room = session.get('room')
	leave_room(room)
	emit('status', {'msg':session.get('name')+ 'has left'}, room='room')



@sockets.on('/echo')
def es(ws):
	print 'socket route /echo'
	while True:
		ws.send('hello socket here i am')



if __name__ == "__main__":
	sockets.run(app)


curl -w "@test.txt" -o /dev/null -s "localhost:8000/hello"

SocketIO is an async API with broadcast messages. Ideal use case for chat room. 
socketio = SocketIO()
socketio.join_room()
socketio.emit()
socketio.leave_room()


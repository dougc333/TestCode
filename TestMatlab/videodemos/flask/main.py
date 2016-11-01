import cv2
from flask import Flask, render_template, Response
from camera import VideoCamera
import time

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    print "gen"
    while True:
	#print 'before camera.get_frame()'
        frame = camera.get_frame()
	#print'after camera.get_frame()'
	#time.sleep(.3)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    c = gen(VideoCamera())
    return Response(c,
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


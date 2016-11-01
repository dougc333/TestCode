
import cv2
import cv

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture("video.mov")
        self.numFrames = 0

    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        print 'numFrames:', self.numFrames
        if self.numFrames == 528:
            self.video = cv2.VideoCapture("video.mov")
            self.numFrames = 0
        self.numFrames += 1
        success, image = self.video.read()

	#this is in raw image format

        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()


import cv2

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture("visiontraffic.avi")
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        success, image = self.video.read()
        
	#this is in raw image format

        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

from imutils.video import VideoStream
from flask import Response
from flask import Flask
from flask import render_template
import PoseModule as pm
import imutils
import time
import cv2
import mediapipe as mp
import numpy as np
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose


# initialize a flask object
app = Flask(__name__)



@app.route("/")
def index():
	# return the rendered template
	return "hi"

def calculate_angle(a,b,c):
    a = np.array(a) # First
    b = np.array(b) # Mid
    c = np.array(c) # End
    
    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(radians*180.0/np.pi)
    
    if angle >180.0:
        angle = 360-angle
        
    return angle
		
def generate():
	
	# loop over frames from the output stream
    vs = VideoStream().start()
    detector = pm.poseDetector()
    count = 0
    direction =0 
    prev_per = 0
    e = 0
    
    while True:
        img = vs.read()
        img = cv2.resize(img, (800,600))
	    #img = cv2.imread("img/test.jpg") 
        img = detector.findPose(img, False) # remove false to see all points
        lmList = detector.findPosition(img, False) #list of 32 points

        if len(lmList) != 0:
            angle = detector.findAngle(img, 11, 13, 15)
            per = np.interp(angle, (40, 170), (100, 0))
            #print(angle, per)
            ##ERRORS##
            
            if direction == 0:#going up
                if prev_per > per: 
                    e+=1

                if(e == 20):
                    print('Lift your arm higher')
                    e= 0
            
            if direction == 1:#going down
                if prev_per < per: 
                    e+=1

                if(e == 20):
                    print('lower your arm')
                    e= 0
                    
            #counting
            if per == 100: 
                if direction == 0:
                    count += 0.5
                    direction = 1

            if per == 0:
                if direction == 1:
                    count+=0.5
                    direction = 0

            prev_per = per

            cv2.putText(img, str(count), (50,100), cv2.FONT_HERSHEY_PLAIN, 5, (255,0,0),4)
        (flag, encodedImage) = cv2.imencode(".jpg",img)
        if not flag:
                continue
        yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encodedImage) + b'\r\n')
    # cv2.waitKey(1)
    # vs.stop()
 		
 
 
 
	# vs = VideoStream().start()
	# time.sleep(2.0)
	# while True:
	# 		frame = vs.read()
	# 		(flag, encodedImage) = cv2.imencode(".jpg",frame)
   
	# 		if not flag:
    # 				continue

	# 		yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encodedImage) + b'\r\n')

@app.route("/video_feed")
def video_feed():
	# return the response generated along with the specific media
	# type (mime type)
	return Response(generate(),
		mimetype = "multipart/x-mixed-replace; boundary=frame")

if __name__ == '__main__':

	# start the flask app
	app.run(debug=True)

# release the video stream pointer

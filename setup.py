from stopwatch import Stopwatch
from imutils.video import VideoStream
from flask import Response
from flask import Flask,request
from flask import render_template
from flask_cors import CORS
import PoseModule as pm
import imutils
import time
import cv2
import mediapipe as mp
import numpy as np
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from io import BytesIO
import base64

check = False
wrong=[]
pers=[]
start=0
stop=0
l1=[]
l2=[]
err_top=[]
err_bottom=[]
# initialize a flask object
app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    # return the rendered template
    return "hi"


def calculate_angle(a, b, c):
    a = np.array(a)  # First
    b = np.array(b)  # Mid
    c = np.array(c)  # End

    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - \
        np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(radians*180.0/np.pi)

    if angle > 180.0:
        angle = 360-angle

    return angle


def leftBicepCurl():

    # loop over frames from the output stream
    global pers,wrong,err_bottom,err_top
    vs = VideoStream().start()
    stopwatch = Stopwatch()
    detector = pm.poseDetector()
    count = 0
    direction = 0
    prev_per = 0
    e = 0
    pers=[]
    wrong=[]
    text=""
    f=0
    err_top=[]
    err_bottom=[]
    while True:
        global check
        if check:
            check = False
            break
        img = vs.read()
        img = cv2.resize(img, (800, 600))
        # img = cv2.imread("img/test.jpg")
        img = detector.findPose(img, False)  # remove false to see all points
        lmList = detector.findPosition(img, False)  # list of 32 points

        if len(lmList) != 0:
            angle = detector.findAngle(img, 11, 13, 15)
            per = np.interp(angle, (40, 170), (100, 0))
            pers.append(per)
            # print(angle, per)
            ##ERRORS##

            if direction == 0:  # going up
                if prev_per > per:
                    e += 1

                if(e == 20):
                    print('Lift your arm higher')
                    text='Lift your arm higher'
                    f=50
                    wrong.append(len(pers)-1)
                    e = 0

            if direction == 1:  # going down
                if prev_per < per:
                    e += 1

                if(e == 20):
                    print('lower your arm')
                    text='lower your arm'
                    f=50
                    wrong.append(len(pers)-1)
                    e = 0

            # counting
            if per == 100:
                if direction == 0:
                    count += 0.5
                    err_bottom.append(angle)
                    direction = 1

            if per == 0:
                if direction == 1:
                    count += 0.5
                    err_top.append(angle)
                    direction = 0

            prev_per = per
            str(stopwatch)
            if f > 0 and text!="":
                cv2.putText(img,text, (20, 550),
                        cv2.FONT_HERSHEY_PLAIN, 4, (255,255,255), 4)
                f=f-1
            cv2.putText(img, str(count), (50, 100),
                        cv2.FONT_HERSHEY_PLAIN, 7, (255,255,255), 4)
        (flag, encodedImage) = cv2.imencode(".jpg", img)
        if not flag:
            continue
        yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encodedImage) + b'\r\n')
    cv2.waitKey(1)
    vs.stop()

def plank():
    
    # loop over frames from the output stream
    global pers,wrong,start,stop,l1,l2
    vs = VideoStream().start()
    stopwatch = Stopwatch()
    detector = pm.poseDetector()
    e1 = 0
    e2=0
    e22=0
    e3=0
    f=0
    text=""
    l1 = []
    l2 = []
    start = time.time()
    while True:
        global check
        if check:
            check = False
            break
        img = vs.read()
        img = cv2.resize(img, (800,600))
	#img = cv2.imread("img/plank.jpg")
        img = detector.findPose(img,False) # remove false to see all points
        
        lmList = detector.findPosition(img, False) #list of 32 points

        if len(lmList) != 0:
            angle1 = detector.findAngle(img, 11, 13, 15)#	elbow
            angle2 = detector.findAngle(img, 11, 23, 25)#   hip
            angle3 = detector.findAngle(img, 23, 25, 27)#	legs

            l1.append(angle1)
            l2.append(angle2)

            #x`print(angle1, angle2, angle3)
            if not 75<=angle1<=105:
                e1+=1
            if(e1==40):
                print('Place shoulder vertically above your elbow')
                text="Place shoulder vertically above your elbow"
                f=50
                e1 = 0

            if angle2<140:
                e2+=1
            if(e2==40):
                print('Straighten your back. Bring your back DOWN')
                text="Straighten your back. Bring your back DOWN"
                f=50
                e2 = 0 

            if angle2 > 170:
                e22+=1
            if(e22==40):
                print('Straighten your back. Bring your back UP')
                text="Straighten your back. Bring your back UP"
                f=50
                e2=0


            if angle3<=160 :
                e3+=1
            if(e3==40):
                print('Do not bend your knee. Stretch your legs')
                text="Do not bend your knee. Stretch your legs"
                f=50
                e3 = 0


		#cv2.putText(img, str(count), (50,100), cv2.FONT_HERSHEY_PLAIN, 5, (255,0,0),4)
        if f > 0 and text!="":
                cv2.putText(img,text, (20, 550),
                        cv2.FONT_HERSHEY_PLAIN, 2, (255,255,255), 2)
                f=f-1
        (flag, encodedImage) = cv2.imencode(".jpg", img)
        if not flag:
            continue
        yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encodedImage) + b'\r\n')
    stop = time.time()
    cv2.waitKey(1)
    vs.stop()
    
def pushups():
    
    # loop over frames from the output stream
    global start,stop,pers,wrong,err_top,err_bottom
    vs = VideoStream().start()
    stopwatch = Stopwatch()
    detector = pm.poseDetector()
    count = 0
    direction = 0  # 0 if gng down, 1 if gng up
    prev_per = 0
    e = 0
    d = 0
    d1=0
    d2=0
    d3=0
    l1 = []
    l2 = []
    f=0
    text=""
    err_top=[]
    err_bottom=[]
    start=time.time()
    while True:
        global check
        if check:
            check = False
            break
        img = vs.read()
        img = cv2.resize(img, (800, 600))
        img = detector.findPose(img, False)  # remove false to see all points

        lmList = detector.findPosition(img, False)  # list of 32 points

        if len(lmList) != 0:
            elbowAngle = detector.findAngle(img, 12, 14, 16)
            buttAngle = detector.findAngle(img, 12, 24, 26)
            legAngle = detector.findAngle(img, 24, 26, 28)
            #elbowAngle = detector.findAngle(img, 11, 13, 15)
            #buttAngle = detector.findAngle(img, 11, 23, 25)
            #legAngle = detector.findAngle(img, 23, 25, 27)

            per = np.interp(elbowAngle, (80, 160), (100, 0))
            # print(angle, per)
            ##ERRORS##
            if direction == 0:
                # elbow>165
                # but>160
                # leg>170
                if legAngle<155:
                    #cv2.putText(img, "make ur legs straighter", (0,100), cv2.FONT_HERSHEY_PLAIN, 5, (255,0,0),4)
                    d1+=1
                if(d1==40):
                    print('make your legs straighter')
                    text="make your legs straighterDown"
                    f=50
                    d1=0
                if buttAngle<155:
                    #cv2.putText(img, "make ur butt straighter", (0,100), cv2.FONT_HERSHEY_PLAIN, 5, (255,0,0),4)
                    d+=1
                if(d==50):
                    print('make your back straight.')
                    text="make your back straight."
                    f=50 
                    d=0         
                
                if prev_per > per: 
                    e+=1

                if(e == 40):
                    print('bring your chest closer to the ground!')
                    text="bring your chest closer to the ground!"
                    f=50 
                    e= 0
                    
            if direction == 1:#going up
                # elbow<40
                # but>160
                # leg>170
                if legAngle<155:
                    #cv2.putText(img, "make ur legs straighter", (0,100), cv2.FONT_HERSHEY_PLAIN, 5, (255,0,0),4)
                    d2+=1
                if(d2==40):
                    print('make your legs straighter')
                    text="make your legs straighter"
                    f=50 
                    d2=0
                if buttAngle<155:
                    #cv2.putText(img, "make ur butt straighter", (0,100), cv2.FONT_HERSHEY_PLAIN, 5, (255,0,0),4)
                    d3+=1
                if(d3==50):
                    print('make your back straight.')
                    text="make your back straight."
                    f=50
                    d3=0          
                            

                if(prev_per > per):
                    e+=1
                if(e==40):
                    print('Higher! Straighten your hands')
                    text='Higher! Straighten your hands'
                    f=50
                    e= 0
                        
            # counting
            if elbowAngle <= 70: 
                if direction == 0:
                    count += 0.5
                    err_bottom.append(elbowAngle)
                    direction = 1

            if elbowAngle >= 165:
                if direction == 1:
                    count+=0.5
                    err_top.append(elbowAngle)
                    direction = 0

            prev_Angle = elbowAngle
            if f > 0 and text!="":
                cv2.putText(img,text, (20, 550),
                        cv2.FONT_HERSHEY_PLAIN, 2, (255,255,255), 2)
                f=f-1
            cv2.putText(img, str(count), (50,100), cv2.FONT_HERSHEY_PLAIN, 5, (255,0,0),4)
  
        (flag, encodedImage) = cv2.imencode(".jpg", img)
        if not flag:
            continue
        yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encodedImage) + b'\r\n')
    stop = time.time()
    cv2.waitKey(1)
    vs.stop()



@app.route("/video_feed")
def video_feed():
    # return the response generated along with the specific media
    # type (mime type)
    if request.args.get("key")=="Left Bicep Curl":
        print(leftBicepCurl())
        return Response(leftBicepCurl(),
                        mimetype="multipart/x-mixed-replace; boundary=frame")
    elif request.args.get("key")=="Right Bicep Curl":
        return Response(rightBicepCurl(),
                        mimetype="multipart/x-mixed-replace; boundary=frame")
    elif request.args.get("key")=="Plank":
        return Response(plank(),
                        mimetype="multipart/x-mixed-replace; boundary=frame")
    elif request.args.get("key")=="Pushups":
        return Response(pushups(),
                        mimetype="multipart/x-mixed-replace; boundary=frame")


@app.route("/results")
def results():
    global check,pers,wrong,start,stop,l1,l2,err_bottom,err_top
    if request.args.get("key")=="Left Bicep Curl":
        img = BytesIO()
        check = True
        top=np.array(err_top)
        bottom=np.array(err_bottom)
        x=np.array([i for i in range(max(len(err_top),len(err_bottom)))])
        plt1=plt.subplot2grid((1,2),(0,0),colspan=1)
        plt2=plt.subplot2grid((1,2),(0,1),colspan=1)
        plt1.axhline(y = 170, color = 'r', linestyle = 'dashed',label = "minimum ideal angle at the top")
        plt2.axhline(y = 40, color = 'g', linestyle = 'dashed',label = "maximum ideal angle at the bottom")
        plt1.plot(np.array([i/40 for i in range(len(err_top))]),top,color="blue",linewidth = 1,label = "user position at the top")
        plt2.plot(np.array([i/40 for i in range(len(err_bottom))]),bottom,color="blue",linewidth = 1, label = "user position at the top")
        plt1.set_ylim(100,200)
        plt2.set_ylim(30,70)
        plt1.set_xlabel('time')
        plt2.set_xlabel('time')

        # naming the y axis
        plt1.set_ylabel('accuracy')
        plt2.set_ylabel('accuracy')

        plt1.set_title('Accuracy of position(top)')
        plt2.set_title('Accuracy of position(bottom)')


        plt1.legend()
        plt2.legend()
        plt.savefig(img, format='png')
        plt.close()
        img.seek(0)
        plot_url = base64.b64encode(img.getvalue()).decode('utf8')
        wrong=[]
        pers=[]
        start=0
        stop=0
        l1=[]
        l2=[]
        err_top=[]
        err_bottom=[]
        return plot_url
    
    elif request.args.get("key")=="Right Bicep Curl":
        return None
    elif request.args.get("key")=="Plank":
        img = BytesIO()
        check = True
        duration = stop - start
        d = len(l1)//duration
        plot1 = plt.subplot2grid((1, 2), (0, 0), colspan=1)
        plot2 = plt.subplot2grid((1, 2), (0, 1), colspan=1)
        
        # Using Numpy to create an array x
        x = [i/d for i in range(len(l1))] 

        plot2.plot(x, l1)
        plot2.set_xlabel("Time")
        plot2.set_ylabel("Accuracy")
        plot2.axhline(y = 80, color = 'g', linestyle = '-', label = "Ideal position of the elbow")
        plot2.set_title('Accuracy of the Elbow')

        plot1.plot(x, l2)
        plot1.set_xlabel("Time")
        plot1.set_ylabel("Accuracy")
        plot1.axhline(y = 160, color = 'r', linestyle = '-', label = "Ideal position of the elbow")
        plot1.set_title('Accuracy of the Back')
        plt.savefig(img, format='png')
        plt.close()
        img.seek(0)
        plot_url = base64.b64encode(img.getvalue()).decode('utf8')
        wrong=[]
        pers=[]
        start=0
        stop=0
        l1=[]
        l2=[]
        err_top=[]
        err_bottom=[]
        return plot_url
    elif request.args.get("key")=="Pushups":
        img = BytesIO()
        check = True
        duration = stop - start
        top=np.array(err_top)
        bottom=np.array(err_bottom)
        d=len(top)//duration

        x=np.array([i for i in range(max(len(err_top),len(err_bottom)))])

        plt1=plt.subplot2grid((1,2),(0,0),colspan=1)
        plt2=plt.subplot2grid((1,2),(0,1),colspan=1)

        plt1.axhline(y = 167, color = 'r', linestyle = 'dashed',label = "ideal position at the top")
        plt2.axhline(y = 69, color = 'g', linestyle = 'dashed',label = "ideal position at the bottom")
        plt1.plot(np.array([i/40 for i in range(len(err_top))]),top,color="blue",linewidth = 1,label = "user position at the top")
        plt2.plot(np.array([i/40 for i in range(len(err_bottom))]),bottom,color="yellow",linewidth = 1, label = "user position at the top")
        plt1.set_ylim(100,200)
        plt2.set_ylim(50,100)

        plt1.set_xlabel('time')
        plt2.set_xlabel('time')

        # naming the y axis
        plt1.set_ylabel('accuracy')
        plt2.set_ylabel('accuracy')

        plt1.set_title('Accuracy of position(top)')
        plt2.set_title('Accuracy of position(bottom)')


        plt1.legend()
        plt2.legend()
        plt.savefig(img, format='png')
        plt.close()
        img.seek(0)
        plot_url = base64.b64encode(img.getvalue()).decode('utf8')
        wrong=[]
        pers=[]
        start=0
        stop=0
        l1=[]
        l2=[]
        err_top=[]
        err_bottom=[]
        return plot_url
        return None
        


if __name__ == '__main__':

    # start the flask app
    app.run(debug=True)

# release the video stream pointer

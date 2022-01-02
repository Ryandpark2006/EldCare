import cv2 as cv
import time
import pose
import numpy as np

cap = cv.VideoCapture('Pose Estimation/GoodMSRDailyActivity3D/Falling/IMG-2069.MOV.avi')
detector = pose.poseDetector(mode=False, upBody=False, smooth=True, detectionCon=0.7, trackCon=0.6)

#steps to downloading processed video

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))    

size = (frame_width, frame_height)

result = cv.VideoWriter('filename.avi', cv.VideoWriter_fourcc(*'MJPG'), 10, size)    #make a counter for later so that it changes the file name when you use a while loop to process all the videos

while True:
    success, img = cap.read()
    if not success:
        break
    img = detector.findPose(img)
    lmList = detector.findPosition(img, draw=False)
    # print(lmList)
    print(lmList) #this gives you all the coordinates at point 14 given in mediapipe website   //make something for if the point doesn't exist

    result.write(img) 
    cv.imshow("Image", img) 
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

result.release()
cap.release()
cv.destroyAllWindows()


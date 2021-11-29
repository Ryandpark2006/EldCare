import cv2 as cv
import time
import pose
import numpy as np

cap = cv.VideoCapture(0)
pTime = 0
detector = pose.poseDetector()
while True:
    success, img = cap.read()
    img = detector.findPose(img)
    lmList = detector.findPosition(img, draw=False)
    # print(lmList)
    print(lmList[14]) #this gives you all the coordinates at point 14 given in mediapipe website   //make something for if the point doesn't exist
    cv.circle(img, (lmList[14][1], lmList[14][2]), 15, (0, 0, 255), cv.FILLED)
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    img =  cv.flip(img, 1)
    cv.putText(img, str(int(fps)), (70,50), cv.FONT_HERSHEY_PLAIN, 3, (255,255,255), 3)
    cv.imshow("Image", img) 
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        break



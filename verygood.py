#go to mediapipe website to see which point corresponds to which number 

import cv2 as cv
import mediapipe as mp
import time
import numpy as np
from tensorflow.keras.models import load_model

class poseDetector():

    def __init__(self, mode = False, upBody = False, smooth = True, detectionCon = 0.5, trackCon = 0.5):

        # self.mode = mode
        # self.upBody = upBody
        # self.smooth = smooth
        # self.detectionCon = detectionCon
        # self.trackCon = trackCon

        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose()

    def findPose(self, img, draw = True):
        imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        blank = np.zeros(img.shape, dtype='uint8')
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(blank, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
        return blank

    def findPosition(self, img, draw = True):
        lmList = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                # print(id, lm)
                cx, cy = int(lm.x * w), int(lm.y * h)   #might be able to get z-values and visibility values if you want
                lmList.append([id, cx, cy])
                if draw:
                    cv.circle(img, (cx, cy), 5, (255, 0, 0), cv.FILLED)
        return lmList
    

def main():
    cap = cv.VideoCapture(0)
    pTime = 0
    detector = poseDetector()
    #model = load_model('/Users/ajaykhanna/Downloads/final.h5')
    # Load class names
    classNames = ['Falling', 'Lyingdown', 'Jumping Jacks' 'Sitting', 'Standing', 'Walking']
    #classNames = ['Standing']
    #print(classNames)
    current = []
    x = 0
    while True:
        success, img = cap.read()
        img = detector.findPose(img)
        lmList = detector.findPosition(img, draw=False)
        img = cv.resize(img, (112, 112))
        if x == 0:
            current = np.array(img)
            x += 1
        elif x == 1:
            arr = np.append(current, img)
            x += 1
        elif x < 5:
            arr = np.append(arr, img)
            x += 1
            #print(current.shape)
            #print(arr.shape)
        else:
            arr = np.roll(arr, -1)
            np.delete(arr, 5)
            arr.resize((1, 5, 112, 112, 3), refcheck=False)
            x += 1
            #print(arr.shape)
        # print(lmList)
        # print(lmList[14]) #this gives you all the coordinates at point 14 given in mediapipe website
        #print(lmList) #this gives you all the coordinates at point 14 given in mediapipe website
        # cv.circle(img, (lmList[14][1], lmList[14][2]), 15, (0, 0, 0), cv.FILLED)

        cTime = time.time()
        fps = 1/(cTime - pTime)
        pTime = cTime

        cv.putText(img, "FPS: " + str(int(fps)), (5,105), cv.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1)

        #cv.imshow("Image", img) 
        # Predict gesture in Hand Gesture Recognition project
        if x >= 6 and x < 46:
            #print(arr.shape)
            #print(arr.shape)
            # prediction = model.predict(arr)
            # classID = np.argmax(prediction)
            # className = classNames[classID]
            # print(className)
    # show the prediction on the frame
            cv.putText(img, str("Standing"), (5, 15), cv.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1)
            #print("hi")
            #cv.putText(img, str(int(prediction)), (30,50), cv.FONT_HERSHEY_PLAIN, 3, (255,0,0), 3)
            #cv.putText(img, str(className), (10,50), cv.FONT_HERSHEY_PLAIN, 3, (255,0,0), 3)
            x += 1
        elif x >= 46 and x < 86:
            cv.putText(img, str("Walking"), (5, 15), cv.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1)
        elif x >= 86 and x < 126:
            cv.putText(img, str("Sitting"), (5, 15), cv.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1)
        elif x >= 126 and x < 166:
            cv.putText(img, str("Falling"), (5, 15), cv.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1)
        elif x >= 166 and x < 206:
            cv.putText(img, str("Lying Down"), (5, 15), cv.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1)
        elif x >= 206 and x < 246:
            cv.putText(img, str("Jumping Jacks"), (5, 15), cv.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1)
        cv.imshow("Image", img) 
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

if __name__ == "__main__":
    main()
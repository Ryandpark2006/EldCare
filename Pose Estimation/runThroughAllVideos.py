import os
import cv2 as cv
import time
import pose
import numpy as np

path = r"C:\Users\user\projects\TJHSST-Science-Fair-Project\Pose Estimation\dataset\Walking"
directory = os.fsencode(path)
count = 0
    
for file in os.listdir(directory):
     filename = os.fsdecode(file)
     if filename.endswith(".mp4") or filename.endswith(".avi"): 
        print(filename)   # prints out which video files are processed
        cap = cv.VideoCapture("Pose Estimation/dataset/Walking/" + filename)
        detector = pose.poseDetector(mode=False, upBody=False, smooth=True, detectionCon=0.7, trackCon=0.6)

        # outputting video
        frame_width = int(cap.get(3))
        frame_height = int(cap.get(4))    
        size = (frame_width, frame_height)
        result = cv.VideoWriter('Walking_' + str(count) + '.avi', cv.VideoWriter_fourcc(*'MJPG'), 10, size)

        while True:
            success, img = cap.read()
            if not success:
                break
            img = detector.findPose(img)
            lmList = detector.findPosition(img, draw=False)            

            result.write(img) 
            cv.imshow("Image", img) 
            
            cv.waitKey(1)

        result.release()
        cap.release()
        cv.destroyAllWindows()

        #  print(os.path.join(directory, filename))
        count += 1
        continue
     else:
         continue


# run through standing and videos
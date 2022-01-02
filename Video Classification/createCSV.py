import os
import cv2 as cv
import csv 
import numpy as np

path = r"C:\Users\user\projects\TJHSST-Science-Fair-Project\Video Classification\Processed\Walking"
directory = os.fsencode(path)
count = 0
f = open('C:/Users/user/projects/TJHSST-Science-Fair-Project/Video Classification/train(1).csv', 'w')
writer = csv.writer(f)


for file in os.listdir(directory):
     filename = os.fsdecode(file)
     if filename.endswith(".mp4") or filename.endswith(".avi"): 
        print(filename)   # prints out which video files are processed
        writer.writerow([filename])
        continue
     else:
         f.close()
         continue
        
# run through standing and videos
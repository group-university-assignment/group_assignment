## User: Luke Chambers ##
## Student ID: w16022690 ##
## Date: 02 Apr 2020 ##
## Last Updated: 04 May 2020 ##
## Sources: Learning OpenCV (Book), PythonProgramming.net (Website) ##



# Import libraries required
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Loads raw video of MRI scan
cap = cv2.VideoCapture('BrainMRI.mp4')

def getFrame(sec):
    cap.set(cv2.CAP_PROP_POS_MSEC, sec*1000)
    hasFrames, image = cap.read()
    count = 0
    sec = 0
    # frameRate dictates how often each image of the video will be saved - change higher or lower to suit
    frameRate = 0.7
    count = 1
    success = getFrame(sec)
    # Saves frames as .png instead of .mp4
    while(hasFrames):
        cv2.imwrite("brainscan" + str(count) + ".png", frame)
        count+=1
    # Saves frames incrementally with naming
    while success:
        count = count + 1
        sec = sec + frameRate
        sec = round(sec, 2)
        success = getFrame(sec)
		
		
while(cap.isOpened()):
    ret, frame = cap.read()
    # New variable to convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  
    # Window to display image
    cv2.imshow('frame', gray)
	
    # Enables writing on image
    font = cv2.FONT_HERSHEY_PLAIN = 1
    cv2.putText(gray, 'PatientName', (0, 130), font,
                1, (200, 255, 155), 2, cv2.LINE_AA)
    # User can use 'q' for 'quit' to break the loop early, similar to abort command above but during the video
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
		
# GaussianBlur to Preserve Image Edges Vital for Diagnosis
blur = cv2.GaussianBlur(res, (15, 15), 0)
cv2.imshow('Gaussian Blurring', blur)

###Tumour Finding Brute Force Algorithm - Homography Feature Matching###

# Tumor Image
img1 = cv2.imread('tumorimage.png', 0)

# Patient Scan Image
img2 = cv2.imread('brainframe1.png', 0)

# Image Detector finds key points and descriptors
orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

# NORM_HAMMING used as it is more computationally efficient
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# Matches Created from BFMatcher and sorted by distance
matches = bf.match(des1, des2)
matches = sorted(matches, key=lambda x: x.distance)

# First 5 matches selected and shown
img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:5], None, flags=2)

# Images displayed together with matches or non-matches for human persual and approval
plt.imshow(img3)
plt.show()
cap.release()
out.release()
cv2.destroyAllWindows()
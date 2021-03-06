import numpy as np
import cv2
from collections import deque

# default call traker function
def setValues(x):
	print("")

# Creating  the trackbars needed for
# adjusting the marker color these
# trackbers will be used for setting
# the upper and lower ranges of the
# HSV required for particular color

cv2.namedWindow("Color detectors")
cv2.createTrackbar("Upper Hue", "Color detectors", 153, 180, setValues)
cv2.createTrackbar("Upper Saturation", "Color detectors", 255, 255, setValues)
cv2.createTrackbar("Upper Value", "Color detectors", 255, 255, setValues)
cv2.createTrackbar("Lower Hue", "Color detectors", 64, 180, setValues)
cv2.createTrackbar("Lower Saturation", "Color detectors", 72, 255, setValues)
cv2.createTrackbar("Lower Value", "Color detectors", 49, 255, setValues)

# Giving different arrays to handle color
# points of different color these arrays
# will holds the points of a particular color
# in the array which will further be used
# in draw on canvas
bpoints = [deque(maxlen = 1024)]
gpoints = [deque(maxlen = 1024)]
rpoints = [deque(maxlen = 1024)]
ypoints = [deque(maxlen = 1024)]

# These indexes will be used to mark position
# of pointers in color array
blue_index = 0
green_index = 0
red_index = 0
yellow_index = 0

# The kernel to be used for dialation purpose
kernel = np.ones((5, 5), np.uint8) 

# The colors which will be used as link for
# the drawing purpose
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 255, 255)]
colorIndex = 0

# Here is code for Canvas Setup
paintWindow = np.zeros((471, 636, 3)) + 255

cv2.namedWindow("Paint", cv2.WINDOW_AUTOSIZE)


# Loading the deafult webcam for PC
cap = cv2.VideoCapture(0)
# Keep looping
while True:
	# Reading the frame from the camera
	ret, frame = cap.read()
	# Flipping the frame to see same side of yours
	frame = cv2.flip(frame, 1)
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	# Getting the updated position of the trackbar
	# and setting the HSV values
	u_hue = cv2.getTrackbarPost("Upper Hue", "Color detectors")
	u_saturation = cv2.getTrackbarPost("Upper Saturation", "Color detectors")
	u_value = cv2.getTrackbarPost("Upper Value", "Color detectors")
	l_hue = cv2.getTrackbarPost("Lower Hue", "Color detectors")
	l_saturation = cv2.getTrackbarPost("Loer Saturation", "Color detectors")
	l_value = cv2.getTrackbarPost("Lower Value", "Color detectors")
	Upper_hsv = np.array([u_hue, u_saturation, u_value])
	Lower_hsv = np.array([l_hue, l_saturation, l_value])
	# Adding the color button to the live frame
	# for coloe access
	frame = cv2.rectangle(frame, (40, 1), (140, 65), (122, 122, 122), -1)
	frame = cv2.rectangle(frame, (160, 1), (255, 65), colors[0], -1)
	frame = cv2.rectangle(frame, (275, 1), (370, 65), colors[1], -1)
	frame = cv2.rectangle(frame, (390, 1), (485, 65), colors[2], -1)
	frame = cv2.rectangle(frame, (505, 1), (600, 65), colors[3], -1)


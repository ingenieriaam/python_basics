import cv2
import face_recognition as fr
from utils import *

####################################################
# Load image
ctrl_photo = fr.load_image_file('image/FotoA.jpg')
probe_photo = fr.load_image_file('image/FotoC.jpg')

####################################################
# change color space
ctrl_photo = cv2.cvtColor(ctrl_photo, cv2.COLOR_BGR2RGB)
probe_photo = cv2.cvtColor(probe_photo, cv2.COLOR_BGR2RGB)

####################################################
# Find control face location
ctrl_face_encoding  = find_face_location(ctrl_photo)
probe_face_encoding = find_face_location(probe_photo)

####################################################
# Compare
result = fr.compare_faces([ctrl_face_encoding], probe_face_encoding, tolerance=0.6)

####################################################
# Measure distance (default is 0.6)
distance = fr.face_distance([ctrl_face_encoding], probe_face_encoding)

####################################################
# Show results
site       = (50, 50)
font       = cv2.FONT_HERSHEY_COMPLEX
font_scale = 0.5
font_color = (0, 255, 0)
font_width = 2

cv2.putText(probe_photo, 
            f'Comparison: {result} Dist: {distance.round(2)}', 
            site,font, 
            font_scale, font_color, 
            font_width)

####################################################
# Show images
cv2.imshow('Control photo', ctrl_photo)
cv2.imshow('Probe photo', probe_photo)
# Hold the window open until a key is pressed
cv2.waitKey(0)

####################################################

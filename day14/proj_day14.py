import cv2
import face_recognition as fr
from utils import *
import os
import time
import numpy as np

#########################################################
# Load images
path = r'image\Empleados'
myImages = []
employees_names = []
employees_list = os.listdir(path)
for employee in employees_list:
    current_img = cv2.imread(f'{path}\{employee}')
    myImages.append(current_img)
    employees_names.append(os.path.splitext(employee)[0])

#########################################################
# Encoding images
employees_encoding_list = encoding_image(myImages)

#########################################################
print('Get ready to take a picture')
time.sleep(3)
# Take webcam images
capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# read image
success, image = capture.read()
if not success:
    print("No image")
else:
    face_capture  = fr.face_locations(image)
    face_encoding = fr.face_encodings(image, face_capture)

    for face_enc, face_loc in zip(face_encoding, face_capture):
        coincidence = fr.compare_faces(employees_encoding_list, face_enc)
        distance    = fr.face_distance(employees_encoding_list, face_enc)
        # the minimal distance is the best match
        coincidence_idx = np.argmin(distance)
        if coincidence[coincidence_idx] > 0.6:
            print('Not coincidence with employees database')
        else:
            print('Welcome !!!')
            name = employees_names[coincidence_idx]

            y1, y2, x1, x2 = face_loc
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(image, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(image, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255))
            
            record_income(name)
            cv2.imshow(name, image)
            cv2.waitKey(0)

#########################################################
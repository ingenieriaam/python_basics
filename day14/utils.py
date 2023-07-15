import cv2
import face_recognition as fr
from datetime import datetime

def find_face_location(photo):
    """
    Find the location of a face in a given photo and draw a rectangle around it.

    Parameters:
    - photo: A numpy array representing an image containing a face.

    Returns:
    - ctrl_face_encoding: A numpy array representing the face encoding of the found face.
    """
    ctrl_face_location = fr.face_locations(photo)[0]
    ctrl_face_encoding = fr.face_encodings(photo)[0]

    top_left_corner     = (ctrl_face_location[3], ctrl_face_location[0])
    bottom_right_corner = (ctrl_face_location[1], ctrl_face_location[2])
    rectangle_color     = (0, 255, 0)
    border_width        = 2

    # Draw rectangles around the face
    cv2.rectangle(photo, 
                top_left_corner, 
                bottom_right_corner, 
                rectangle_color, 
                border_width)
    return ctrl_face_encoding

#---------------------------------------------------------

def encoding_image(images):
    """
    Takes a list of images and returns a list of their encodings.
    
    Parameters:
        images (List[array]): A list of images to encode.
        
    Returns:
        encoding_list (List[array]): A list of encodings for each input image.
    """
    encoding_list = []
    for image in images:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # encoding
        image_encoding = fr.face_encodings(image)[0]
        encoding_list.append(image_encoding)
    return encoding_list

#---------------------------------------------------------
def record_income(person):
    f = open('registry.csv', 'r+') # open file in read and write mode
    data_list = f.readlines()
    name_reg = []
    for line in data_list:
        income = line.split(',')
        name_reg.append(income[0])
    
    if person not in name_reg:
        now = datetime.now()
        stringNow = now.strftime("%H:%M:%S")
        f.writelines(f'\n{person},{stringNow}')
import cv2
import os
import numpy as np
import cvlib as cv
from django.conf import settings
from keras.models import model_from_json
from keras.preprocessing import image
from .import *
face_detection_videocam = cv2.CascadeClassifier(os.path.join(
settings.BASE_DIR,'haarcascade_frontalface_default.xml'))

model = model_from_json(open(os.path.join(settings.BASE_DIR,'myapp/fer.json'), "r").read())
model.load_weights(os.path.join(settings.BASE_DIR,'myapp/fer.h5'))

def pic(abc):
    path='media/media/abc/'+str(abc)
    print(path,type(path))
    img=cv2.imread(os.path.join(settings.BASE_DIR,str(path)))
    #img=cv2.resize(img,(640,640))
    faces, confidences = cv.detect_face(img)
    for face in faces:
        (startX,startY) = face[0],face[1]
        (endX,endY) = face[2],face[3]    # draw rectangle over face
        cv2.rectangle(img, (startX,startY), (endX,endY), (0,255,0), 2)
        #cv2.rectangle(img, pt1=(x, y), pt2=(x + w, y + h), color=(255, 0, 0), thickness=5)
        roi_gray=img[startX:endX,startY:endY]#cropping region of interest i.e. face area from  image
        try:
            roi_gray=cv2.cvtColor(roi_gray,cv2.COLOR_BGR2GRAY)
            roi_gray=cv2.resize(roi_gray,(48,48))
            img_pixels = image.img_to_array(roi_gray)
            img_pixels = np.expand_dims(img_pixels, axis = 0)
            img_pixels /= 255
            predictions = model.predict(img_pixels)
            max_index = np.argmax(predictions[0])
            emotions = ('angry', 'disgust', 'fear', 'Happy', 'sad', 'surprise', 'normal')
            predicted_emotion = emotions[max_index]
            cv2.putText(img, predicted_emotion, (int(startX), int(startY)), cv2.FONT_HERSHEY_SIMPLEX, 3, (0,0,255), 5)
        except:
            return False
    cv2.imwrite(os.path.join(settings.BASE_DIR,str(path)),img)
    print("success")
    return True

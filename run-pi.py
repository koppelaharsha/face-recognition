import cv2
from picamera import PiCamera
from picamera.array import PiRGBArray
from datetime import datetime
from .aws.rekognition.faces import search_face
from .aws.dynamoDB.items import get_item

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

camera = PiCamera()
rawCapture = PiRGBArray(camera)

while True:
    camera.capture(rawCapture, format="bgr")
    image = rawCapture.array
    #img = cv2.imread('./img-1.jpg')
    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_img,scaleFactor=1.5,minNeighbors=1)
    (x,y,w,h) = (1,30,0,0)
    for (x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,0),2)
        break
    cv2.imshow('image',image)        
    k = cv2.waitKey(10) & 0xFF
    if k == 13:
        font = cv2.FONT_HERSHEY_SIMPLEX
        colour = (255,255,0)
        if len(faces) > 0 :
            image_path = "images/"+"img"+datetime.now().strftime('%Y%m%d%H%M%S')+".jpg"
            cv2.imwrite(image_path, image)
            face = search_face('My-Collection',image_path)
            print(face)
            if face != 'No Match Found':
                print('Match Found')
                name = get_item('Faces',{'face-id':face['Id']})
                print(name)
            else:
                name = 'No Match Found'
        else:
            name = 'No Faces Found'
        cv2.putText(image, name, (x,y-5), font, 1, colour, 2)
        cv2.imshow('image',image)
        cv2.waitKey(1000)
    if k in [ord('q'),27]:
        break

# cap.release()
cv2.destroyAllWindows()

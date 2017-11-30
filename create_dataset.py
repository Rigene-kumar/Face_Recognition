import numpy as np
import cv2

# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades

face_cascade = cv2.CascadeClassifier('Haar/haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
id=str(input('enter user id'))
sampleNum=0

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)	
    for (x,y,w,h) in faces:
	sampleNum=sampleNum+1
	cv2.imwrite("dataset/user."+id+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])        
	cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.waitKey(500)
    cv2.imshow("Face",img)
    cv2.waitKey(0)
    if(sampleNum>2000):
	break

cap.release()
cv2.destroyAllWindows()

import cv2,time
import pyautogui
import mediapipe
# import urllib
# import numpy as np
face_cascade = cv2.CascadeClassifier("haarcascade.xml")
video = cv2.VideoCapture(0)
# address = "http://192.168.13.98:8080/video"
# video.open(address)
while True:
    _,frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4)
    for x,y,w,h in face:
        img = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow('ROLEX',frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    
    # imgResp = urllib.urlopen(url)
    # imgNp = np.array(bytearray(imgResp.read()),dtype=np.uint8)
    # img = cv2.imdecode(imgNp,-1)
    # cv2.imshow('test',img)
    # cv2.waitKey(10)
video.release()
cv2.destroyAllWindows()
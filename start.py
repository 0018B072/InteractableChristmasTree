import cv2
import numpy as np
from pyzbar.pyzbar import decode

#img = cv2.imread('1.png') #add the names to a list, have it auto select
#img2 = cv2.imread('Day_1.png')
#list = ['1.png', 'Day_1.png']
cap = cv2.VideoCapture(1)
cap.set(3,640)
cap.set(4,480)
while True:
    success, img2 = cap.read() #img 2 initialized here
    for qrcode in decode(img2):
    #print(qrcode.data) #.data = value, .rect = coord
        myData = qrcode.data.decode('utf-8')
        print(myData)
        pts = np.array([qrcode.polygon], np.int32)
        pts = pts.reshape(-1,1,2)
        cv2.polylines(img2, [pts], True, (255,0,255), 4)
        pts2 = qrcode.rect
        cv2.putText(img2, myData, (pts2[0], pts2[1]),cv2.FONT_HERSHEY_COMPLEX, 0.9, (255,0,255), 2)
    
    cv2.imshow('Result', img2)
    cv2.waitKey(1)
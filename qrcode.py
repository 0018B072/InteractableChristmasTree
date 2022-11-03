import cv2
import numpy as np
import functools
from pyzbar.pyzbar import decode

#img = cv2.imread('1.png') #add the names to a list, have it auto select
#img2 = cv2.imread('Day_1.png')
#list = ['1.png', 'Day_1.png']
cap = cv2.VideoCapture(1)
cap.set(3,640)
cap.set(4,480)

#userInput = input("PRESS 2 for EXIT") add ltr where if you show a certain qr code, it exits
with open('myDataFile.txt') as f: #explore "with" and "as"
    myDataList = f.read().splitlines() #this function is similar to the parsing data in xqcProject
#print(myDataList) (prints out the id's in the text file)

while True:
    

    success, img = cap.read() #img 2 initialized here
    for qrcode in decode(img):
        circle1x = 320
        circle1y = 220
    #print(qrcode.data) #.data = value, .rect = coord
        myData = qrcode.data.decode('utf-8')
        #print(myData)
        pts = np.array([qrcode.polygon], np.int32)
        pts = pts.reshape(-1,1,2)
        pts2 = qrcode.rect
        #coordList = []
        cv2.circle(img, (circle1x,circle1y), 5, (0,0,255), -1)
        #i would have to make origin points for all qrcodes, all origin points will be paired w a qrcode
        #the distance check will be done w the qrcode and assigned origin point
        if(myData in myDataList): #explore "in"
            cv2.polylines(img, [pts], True, (0,255,0), 4)
            cv2.putText(img, myData, (pts2[0], pts2[1]),cv2.FONT_HERSHEY_COMPLEX, 0.9, (0,255,0), 2)
            
            #cv2.circle()

            #coordList.append(qrcode.polygon[0] + qrcode.polygon[1] + qrcode.polygon[2] + qrcode.polygon[3])
            """
            x1=coordList[0]
            x2=coordList[2]
            y1=coordList[1]
            y2=coordList[3] 
            """
            print("AUTHORIZED: ", myData, " | ", "Coordinates: ", qrcode.polygon[0],
                qrcode.polygon[1], qrcode.polygon[2], qrcode.polygon[3])
            print(qrcode.polygon[0]+qrcode.polygon[2])
            res = tuple(map(lambda i, j: (i + j)/2, qrcode.polygon[0], qrcode.polygon[2])) #new tuple
            #res2 = functools.reduce(lambda sub, ele: sub * 10 + ele, res)
            print(res)
            cv2.circle(img, (int(res[0]), int(res[1])) , 3, (0,255,0), -1)
            
            print("Distance", np.sqrt((res[0]-circle1x)**2+ (res[1]-circle1y)**2))

           #cv2.circle(img,[res],(0,255,255),2)
            #print(len(coordList))
            #print(type(coordList[0]))
            #print((x1+x2)/2, (y1+y2)/2)

            #cv2.circle(img, ((int(qrcode.polygon[0]) + int(qrcode.polygon[3])))/2,1, (0,255,0), 3)
            #cv2.circle(img, [pts] , 1, (0,255,0), 3)
        else:
            cv2.polylines(img, [pts], True, (0,0,255), 4)
            cv2.putText(img, "ERROR", (pts2[0], pts2[1]),cv2.FONT_HERSHEY_COMPLEX, 0.9, (0,0,255), 2)
            print("DATA: ", myData, " | ", "Coordinates: ", qrcode.rect, " | ", "TYPE: ", "ERROR")
            # what is the difference between "top" and "height"
    cv2.imshow('Result', img)
    cv2.waitKey(1)
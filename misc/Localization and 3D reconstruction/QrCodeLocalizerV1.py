import numpy as np
import cv2
from pyzbar.pyzbar import decode


#opens up the camera, and sets (3,width) and (4, height) to 720p resolution
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)



#while the program is running
while True:


    #setting the img var to the input frame
    success, img =cap.read()
    #decodes the image, finds a qr code
    for barcode in decode(img):
        #prints qr code data into the output
        print(barcode.data)
        #sets barcode data to actual info
        mydata = barcode.data.decode('utf-8')
        #prints human-readable data
        print(mydata)
        #sets corner points of the qr code, in numpy big ole int format
        pts = np.array([barcode.polygon],np.int32)
        #makes the points nice and readable
        pts = pts.reshape((-1,1,2))
        #draws actual lines with the pts variable input
        cv2.polylines(img,[pts],True,(255,0,255),5)
        #assigns the points to a rectangle, so it can be fucked with
        pts2 = barcode.rect
        #uses the recangle arrangement and puts the qr code text on top
        cv2.putText(img,mydata,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX, .9, (255,0,255),2)
    #standard ending crap
    cv2.imshow('Result', img)
    if cv2.waitKey(1) == ord('q'):
        break

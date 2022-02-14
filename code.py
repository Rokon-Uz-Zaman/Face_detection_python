#face detection using opencv Python  

import cv2

faceCascade=cv2.CascadeClassifier(("harrcade_frontalface_default_.xml")
cap=cv2.VideoCapture(0)
while True:
     check,img=cap.read()
     gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
     faces=faceCascade.detectmultiscale(img,1.1,4)
     for(x,y,a,b) in faces :
         cv2.rectangle(img,(x,y),(x+a,y+b),(225,0,0))
         cv2.imshow("img",img)
         k=cv2.waitKey(30) &  0xFF
         if k =27:
            break
                
cv2.destroyAllWindows()                                  
                                   
                                   

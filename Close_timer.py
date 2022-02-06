
from textwrap import fill
import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector

cap = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces = 1)
idlist = [144,145,153,110,157,158,160,161,130,243,386,374,460,398] #386,374*/460,398 left eye ,

while True :
    success,img = cap.read()
    img,faces =detector.findFaceMesh(img,draw = False)
    
    if faces:
        face = faces[0]
        for id in idlist :
            cv2.circle(img,face[id],2,(255,0,255),cv2.FILLED)
    
    cv2.imshow("image",img)
    cv2.waitKey(1)




from textwrap import fill
from turtle import left
import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector

cap = cv2.VideoCapture("video.mp4")
detector = FaceMeshDetector(maxFaces = 1)
idlist = [22,23,24,110,157,158,160,161,130,243,386,359,374,398] #386,374*/460,398 left eye ,
while True :
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES,0 )
    success,img = cap.read()
    img,faces =detector.findFaceMesh(img,draw = False)
    
    if faces:
        face = faces[0]
        for id in idlist :
            cv2.circle(img,face[id],2,(255,0,255),cv2.FILLED)
    
        leftup = face[159]
        leftdown = face [145]
        leftext1 = face[130]
        leftext2 = face[243]
        rightup =face[386]
        rightdown =face[374]
        rightext1 =face[398]
        rightext2 =face[359]
        cv2.line(img,rightdown,rightup,(0,200,0))
        cv2.line(img,rightext1,rightext2,(0,200,0))
        cv2.line(img,leftdown,leftup,(0,200,0))
        cv2.line(img,leftext1,leftext2,(0,200,0))

        lengthleft,_=detector.findDistance(leftup,leftdown)
        lengthright,_ =detector.findDistance(rightup,rightdown)
        hightleft,_ = detector.findDistance(leftext1,leftext2)
        hightright,_ =detector.findDistance(rightext1,rightext2)
        print("left ratio",hightleft/lengthleft ,"right ration", hightright/lengthright)
    cv2.imshow("image",img)
    cv2.waitKey(1)



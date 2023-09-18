import cv2
from cvzone.HandTrackingModule import HandDetector
import time
import pyautogui

detector = HandDetector(detectionCon=0.8,maxHands=2,modelComplexity=1,minTrackCon=0.5)

video = cv2.VideoCapture(0)
a=0
while True:
    ret,frame = video.read()
    hands,img=detector.findHands(frame)
    if hands:
        leftHand = hands[0]
        if len(hands) ==2:
            rightHand = hands[1]
            fingersR=detector.fingersUp(rightHand)
            fingersL=detector.fingersUp(leftHand)

            if fingersR==[0,0,0,0,0]:
                pyautogui.keyDown('right')
                pyautogui.keyUp('left')
            elif fingersL==[0,0,0,0,0]:
                pyautogui.keyDown('left')
                pyautogui.keyUp('right')
            elif fingersR==[1,1,1,1,1] and fingersL==[1,1,1,1,1]:
                pyautogui.keyUp('left')
                pyautogui.keyUp('right')
            
    cv2.imshow("Frame",frame)
    cv2.waitKey(1)
    if a == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
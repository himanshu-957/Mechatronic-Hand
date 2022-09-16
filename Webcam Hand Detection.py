import cv2
from cvzone.HandTrackingModule import HandDetector
cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands = 1, detectionCon = 0.5)
while True:
    ret, frame = cap.read()
    hands, frame = detector.findHands(frame)
    if hands:
        lmlist = hands[0]
        if lmlist:
               
            fingerup = detector.fingersUp(lmlist)
            print(fingerup)
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Image",frame)
    cv2.waitKey(1)

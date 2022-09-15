import cv2
from cvzone.HandTrackingModule import HandDetector
cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands = 1, detectionCon = 0.5)
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    hands, frame = detector.findHands(frame)
    if hands:
        lmlist = hands[0]
        if lmlist:
               
              # Find how many fingers are up
            # This function return list
            fingerup = detector.fingersUp(lmlist)
            print(fingerup)
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Image",frame)
    cv2.waitKey(1)

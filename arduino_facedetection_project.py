import cv2
from cvzone.FaceDetectionModule import FaceDetector
from cvzone.SerialModule import SerialObject

c = cv2.VideoCapture(0)
detector = FaceDetector()
ard = SerialObject()

while True:
    success, img = c.read()
    img, bBxoes = detector.findFaces(img) 

    if bBxoes:
        ard.sendData([1,0])
    else:
        ard.sendData([0,1])

    if cv2.waitKey(1) & 0xFF == ord('d'):
        break

    cv2.imshow("Video", img)

    cv2.waitKey(1)

cv2.destroyAllWindows()

import cv2
from cvzone.FaceDetectionModule import FaceDetector
from cvzone.SerialModule import SerialObject

c = cv2.VideoCapture(0) #0 for inbuilt camera
detector = FaceDetector()
ard = SerialObject() #serial object indicates the port to which arduino uno is connected

while True:
    success, img = c.read()
    img, bBxoes = detector.findFaces(img) 

    if bBxoes:
        ard.sendData([1,0]) #if a face is detected, green LED glows and red LED does not glow
    else:
        ard.sendData([0,1]) #if a face is not detected red LED glows and green doesn't

    if cv2.waitKey(1) & 0xFF == ord('d'): #pressing the key 'd' closes the webcam
        break

    cv2.imshow("Video", img)

    cv2.waitKey(1)

cv2.destroyAllWindows()

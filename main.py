import cv2
from PIL import Image
from util import get_limits

# Info de la webcam
cap = cv2.VideoCapture(0)

red = [40, 20, 150]
blue = [30,20,150]

while True:
    ret, frame = cap.read()
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lowerLimit, upperLimit = get_limits(color=red)
    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)
    mask_ = Image.fromarray(mask)
    
    cv2.imshow("frame", mask)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

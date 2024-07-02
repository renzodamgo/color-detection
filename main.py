import cv2
from PIL import Image
# Info de la webcam
cap = cv2.VideoCapture(0)


# print(frame)

while True:
  ret, frame = cap.read()
  cv2.imshow('frame', frame)

  if cv2.waitKey(1) & 0xFF == ord('q'):
    break


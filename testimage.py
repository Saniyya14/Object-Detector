from ObjectDetectorModule import *


cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
while True:
    success, img = cap.read()
    result, objectInfo = getObjects(img, 0.45, 0.2)
    #print(objectInfo)
    cv2.imshow("Output", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Ensure this line is inside the loop
        break


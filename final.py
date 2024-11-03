import cv2
import pyttsx3

classNames = []
classFile = 'coco.names'
with open(classFile, 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath = 'frozen_inference_graph.pb'

net = cv2.dnn_DetectionModel(weightsPath, configPath)
net.setInputSize(320, 320)
net.setInputScale(1.0/127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

def getObjects(img, thresh, nms, draw=False, objects=[]):
    classIds, confs, bbox = net.detect(img, confThreshold=thresh, nmsThreshold=nms)

    if len(objects) == 0:
        objects = classNames

    objectInfo = []
    maxConfidence = -1  # Initialize max confidence to a low value
    maxConfidenceClass = None  # To store the class with the highest confidence

    if len(classIds)!= 0:
        for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
            className = classNames[classId - 1]
            if className in objects:
                objectInfo.append([box, className, confidence])  # Append confidence along with box and className
                if confidence > maxConfidence:
                    maxConfidence = confidence
                    maxConfidenceClass = className  # Update the class with the highest confidence

                if draw and maxConfidenceClass is not None:
                    # Speech synthesis
                    engine = pyttsx3.init()
                    engine.say(f"The thing in front of you is a {className}.")
                    engine.runAndWait()

    return objectInfo

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    cap.set(3, 1280)
    cap.set(4, 720)
    while True:
        success, img = cap.read()
        objectInfo = getObjects(img, 0.45, 0.2, draw=False)
        # No need to display the image anymore
        if cv2.waitKey(1) & 0xFF == ord('q'):  # Ensure this line is inside the loop
            break

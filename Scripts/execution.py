import cv2 as cv
from matplotlib import image
import numpy as np
import os

def createDataset(inputPath, outputPath, findingObject):
    os.chdir(outputPath)
    #print(findingObject)

    path =r"C:\Users\Superm4n\Desktop\YOLO"
    weight = path+r"\yolov3-320\yolov3.weights"
    cfg = path+r"\yolov3-320\yolov3.cfg"
    net = cv.dnn.readNetFromDarknet(cfg,weight)
    classes = []
    with open(path+"\coco.names", "r") as f:
        classes = [line.strip() for line in f.readlines()]
    
    imageCounter = 1

    cap = cv.VideoCapture(inputPath)
    while True:
        ret,img = cap.read()
        img = cv.resize(img,(750,400))

        if ret == False:
            break
        height, width,_ = img.shape
        blob = cv.dnn.blobFromImage(img, 1/255.0, (416, 416), swapRB=True, crop=False)

        net.setInput(blob)

        output_layers_names = net.getUnconnectedOutLayersNames()
        layers_outputs = net.forward(output_layers_names)

        for output in layers_outputs:
            for detection in output:
                scores = detection[5:]
                class_id = np.argmax(scores)

                if classes[class_id] != findingObject:
                    continue

                confidence = scores[class_id]

                if confidence > 0.5:
                    center_x = int(detection[0]*width)
                    center_y = int(detection[1]*height)
                    w = int(detection[2]*width)
                    h = int(detection[3]*height)

                    x = int(center_x - w/2)
                    y = int(center_y - h/2)

                    if w>0 and h>0:
                        savingImg = img[y:y+h, x:x+w]

                        #cv.imshow("test",savingImg)
                        cv.imwrite(findingObject + str(imageCounter) + ".jpg",savingImg)
                        imageCounter += 1

        cv.imshow('image', img)

        if cv.waitKey(1) & 0xFF == ord(' '):
            break

    cap.release()
    cv.destroyAllWindows()

#createDataset(r'C:/Users/Superm4n/Desktop/YOLO/testVid.mp4',r'C:\Users\Superm4n\Desktop\New folder','bicycle')
from imutils.object_detection import non_max_suppression
import numpy as np
import time
import cv2

import os
print(os.path.exists("C:/Users/Dell/OneDrive/Dokumentumok/Beagy_11_hazi/frozen_east_text_detection.pb"))


def decode_predictions(scores, geometry, probThr=0.8):
    (numRows, numCols) = scores.shape[2:4]
    rects = []
    confidences = []

    for y in range(0, numRows):
        scoresData = scores[0, 0, y]
        xData0 = geometry[0, 0, y]
        xData1 = geometry[0, 1, y]
        xData2 = geometry[0, 2, y]
        xData3 = geometry[0, 3, y]
        anglesData = geometry[0, 4, y]
        # loop over the number of columns
        for x in range(0, numCols):
            if scoresData[x] < probThr:
                continue
            (offsetX, offsetY) = (x * 4.0, y * 4.0)
            angle = anglesData[x]

            cos = np.cos(angle)
            sin = np.sin(angle)

            h = xData0[x] + xData2[x]
            w = xData1[x] + xData3[x]

            endX = int(offsetX + (cos * xData1[x]) + (sin *xData2[x]))
            endY = int(offsetY - (sin * xData1[x]) + (cos *xData2[x]))
            startX = int(endX - w)
            startY = int(endY - h)
            rects.append((startX, startY, endX, endY))
            confidences.append(scoresData[x])
    return confidences, rects


def draw_boxes(image, boxes, ration):
    (rW, rH) = ration

    for (startX, startY, endX, endY) in boxes:
        # Scale the bounding box coordinates
        startX = int(startX * rW)
        startY = int(startY * rH)
        endX = int(endX * rW)
        endY = int(endY * rH)
        # Draw the bounding box on the image
        cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)

    # Display the image with bounding boxes
    while True:
        cv2.imshow("Detected Texts", image)
        key = cv2.waitKey(1) & 0xFF
        # Break the loop if 'q' is pressed
        if key == ord("q"):
            break

    cv2.destroyAllWindows()



image = cv2.imread("C:/Users/Dell/OneDrive/Dokumentumok/Beagy_11_hazi/sample.png")
orig = image.copy()
(H, W) = image.shape[:2]

(newW, newH) = (1024, 1024)
rW = W / float(newW)
rH = H / float(newH)
image = cv2.resize(image, (newW, newH))
(H, W) = image.shape[:2]

layerNames = ["feature_fusion/Conv_7/Sigmoid","feature_fusion/concat_3"]

print("[INFO] loading EAST text detector...")

net = cv2.dnn.readNet("C:/Users/Dell/OneDrive/Dokumentumok/Beagy_11_hazi/frozen_east_text_detection.pb")

blob = cv2.dnn.blobFromImage(image, 1.0, (W, H),(123.68, 116.78, 103.94), swapRB=True, crop=False)

start = time.time()
net.setInput(blob)
(scores, geometry) = net.forward(layerNames)
end = time.time()
print("[INFO] text detection took {:.6f} seconds".format(end - start))
confidences, rects = decode_predictions(scores, geometry)
boxes = non_max_suppression(np.array(rects), probs=confidences)
draw_boxes(orig, boxes, (rW, rH))

        

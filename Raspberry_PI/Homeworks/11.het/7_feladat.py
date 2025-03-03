
import time
import cv2
import numpy as np
import pytesseract
from imutils.object_detection import non_max_suppression

# Function to decode predictions from the EAST model
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
        for x in range(0, numCols):
            if scoresData[x] < probThr:
                continue
            (offsetX, offsetY) = (x * 4.0, y * 4.0)
            angle = anglesData[x]
            cos = np.cos(angle)
            sin = np.sin(angle)

            h = xData0[x] + xData2[x]
            w = xData1[x] + xData3[x]

            endX = int(offsetX + (cos * xData1[x]) + (sin * xData2[x]))
            endY = int(offsetY - (sin * xData1[x]) + (cos * xData2[x]))
            startX = int(endX - w)
            startY = int(endY - h)
            rects.append((startX, startY, endX, endY))
            confidences.append(scoresData[x])
    return confidences, rects

# Function to apply OCR and visualize the results
def process_and_visualize(image, boxes, ratio):
    (rW, rH) = ratio
    for (startX, startY, endX, endY) in boxes:
        # Expand the bounding box slightly
        padding = 5  # Adjust padding as needed
        startX = int((startX - padding) * rW)
        startY = int((startY - padding) * rH)
        endX = int((endX + padding) * rW)
        endY = int((endY + padding) * rH)

        # Ensure the coordinates stay within the image boundaries
        startX = max(0, startX)
        startY = max(0, startY)
        endX = min(image.shape[1], endX)
        endY = min(image.shape[0], endY)

        # Extract the ROI
        roi = image[startY:endY, startX:endX]

        # Apply Tesseract OCR to the ROI
        text = pytesseract.image_to_string(roi, config="--psm 7")  # PSM 7 assumes a single line of text
        print(f"Detected text: {text.strip()}")

        # Draw the bounding box and overlay text on the image
        cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)  # Green bounding box
        cv2.putText(image, text.strip(), (startX, startY - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)  # Red text


    # Display the output image
    while True:
        cv2.imshow("Text Detection and Recognition", image)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):  # Check if 'q' key is pressed
            break
    cv2.destroyAllWindows()  # Close all OpenCV windows


# Load the input image
image_path = "C:/Users/Dell/OneDrive/Dokumentumok/Beagy_11_hazi/car.jpg"
image = cv2.imread(image_path)
orig = image.copy()
(H, W) = image.shape[:2]

# Resize image for EAST model
(newW, newH) = (1024, 1024)
rW = W / float(newW)
rH = H / float(newH)
image = cv2.resize(image, (newW, newH))
(H, W) = image.shape[:2]

# Load the pre-trained EAST model
print("[INFO] Loading EAST text detector...")
model_path = "C:/Users/Dell/OneDrive/Dokumentumok/Beagy_11_hazi/frozen_east_text_detection.pb"
net = cv2.dnn.readNet(model_path)

# Prepare the image blob for EAST
blob = cv2.dnn.blobFromImage(image, 1.0, (W, H), (123.68, 116.78, 103.94), swapRB=True, crop=False)
start = time.time()
net.setInput(blob)
(scores, geometry) = net.forward(["feature_fusion/Conv_7/Sigmoid", "feature_fusion/concat_3"])
end = time.time()
print(f"[INFO] Text detection took {end - start:.6f} seconds")

# Decode predictions and suppress overlapping boxes
confidences, rects = decode_predictions(scores, geometry)
boxes = non_max_suppression(np.array(rects), probs=confidences)

# Apply OCR and visualize the results
process_and_visualize(orig, boxes, (rW, rH))

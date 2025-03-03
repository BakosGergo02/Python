import cv2
import imutils
import datetime
import time

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Error: Could not open laptop camera.")
    exit()

time.sleep(2.0)

while True:
    ret, frame = camera.read()

    if not ret:
        print("Error: Could not read frame from camera.")
        break

    frame = imutils.resize(frame, width=400)

    timestamp = datetime.datetime.now()
    ts = timestamp.strftime("%A %d %B %Y %I:%M:%S%p")
    cv2.putText(frame, ts, (10, frame.shape[0] - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

cv2.destroyAllWindows()
camera.release()

from imutils.video import VideoStream
import datetime
import imutils
import time
import cv2
import numpy as np

video_path = None
buffsize = 64
indx = 0

red_range_lower = [(0, 120, 70), (10, 255, 255)]  # Lower range of red
red_range_upper = [(170, 120, 70), (180, 255, 255)]  # Upper range of red

path = np.zeros((buffsize, 2), dtype='int')

video_path = None
if video_path is None:
    vs = VideoStream().start()
    time.sleep(2)
else:
    vs = cv2.VideoCapture(video_path)

while True:
    frame = vs.read()
    frame = frame if video_path is None else frame[1]
    if frame is None:
        break

    frame = imutils.resize(frame, width=500)
    blur = cv2.GaussianBlur(frame, (9, 9), 0)
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

    mask_lower = cv2.inRange(hsv, red_range_lower[0], red_range_lower[1])
    mask_upper = cv2.inRange(hsv, red_range_upper[0], red_range_upper[1])
    mask = cv2.bitwise_or(mask_lower, mask_upper)

    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    if len(cnts) > 0:
        cnt = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(cnt)
        M = cv2.moments(cnt)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        if radius > 10:
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)
            if indx < buffsize:
                path[indx] = (center[0], center[1])
                indx += 1
            else:
                path[0:indx-1] = path[1:indx]
                path[indx-1] = (center[0], center[1])
        else:
            path.fill(0)
            indx = 0
    else:
        path.fill(0)
        indx = 0

    for i in range(1, indx):
        if path[i - 1][0] == 0 or path[i][0] == 0:
            continue
        thickness = int(np.sqrt(i + 1) * 2.5)
        cv2.line(frame, (path[i - 1][0], path[i - 1][1]), (path[i][0], path[i][1]), (0, 0, 255), thickness)

    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

if video_path is None:
    vs.stop()
else:
    vs.release()
cv2.destroyAllWindows()

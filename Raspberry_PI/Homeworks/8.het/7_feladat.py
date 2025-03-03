import cv2
import time

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Error: Could not open camera.")
    exit()

# Allow the camera to warm up
time.sleep(2)

# Discard the first few frames
for _ in range(5):
    camera.read()

ret, frame = camera.read()

if ret:
    cv2.imwrite("test.jpg", frame)
    cv2.imshow("Image", frame)
    cv2.waitKey(0)
else:
    print("Error: Could not read frame from camera.")

camera.release()
cv2.destroyAllWindows()

from pyzbar import pyzbar
import cv2

video_stream = cv2.VideoCapture(0)

if not video_stream.isOpened():
    print("Error: Could not open video stream.")
    exit()

while True:
    ret, frame = video_stream.read()
    if not ret:
        print("Failed to capture video frame.")
        break

    barcodes = pyzbar.decode(frame)

    for barcode in barcodes:
        (x, y, w, h) = barcode.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type

        text = "{} ({})".format(barcodeData, barcodeType)
        cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    cv2.imshow("Barcode and QR Code Detection", frame)

    # exit the loop if q is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_stream.release()
cv2.destroyAllWindows()

from pyzbar import pyzbar
import cv2
import time

# Path to your barcode image
image_path = r"C:/Users/Dell/OneDrive/Dokumentumok/Beagy_8_hazi/barcode.png"  # Update this to where your barcode image is located

# Read the image
image = cv2.imread(image_path)

# Check if image is loaded correctly
if image is None:
    print("Error: Image not found or cannot be opened.")
    exit()

print(f"Image loaded with shape: {image.shape}")  # Debugging: Print image shape

# Add a short delay to allow for any initialization issues
time.sleep(1)  # You can adjust this delay if needed

# Convert the image to grayscale (improves contrast for barcode detection)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding to enhance the contrast (binary thresholding)
_, thresholded_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY)

# Now decode the barcode in the thresholded image
barcodes = pyzbar.decode(thresholded_image)

if len(barcodes) == 0:
    print("No barcodes found in the image.")
else:
    print(f"Found {len(barcodes)} barcode(s).")

# Process the detected barcodes
for barcode in barcodes:
    (x, y, w, h) = barcode.rect
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
    barcodeData = barcode.data.decode("utf-8")
    barcodeType = barcode.type
    text = "{} ({})".format(barcodeData, barcodeType)
    cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

# Show the output image with detected barcodes
cv2.imshow("Barcode Detection", image)

# Wait until any key is pressed to close the window
cv2.waitKey(0)
cv2.destroyAllWindows()

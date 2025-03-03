import pytesseract
import cv2

image = cv2.imread("C:/Users/Dell/OneDrive/Dokumentumok/Beagy_11_hazi/sample.png")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

options = "outputbase digits"
text = pytesseract.image_to_string(rgb, config=options)

options += "-c tessedit_char_whitelist={} ".format("#")
options += "-c tessedit_char_blacklist={}".format("*")
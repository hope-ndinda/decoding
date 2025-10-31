import cv2
from pylibdmtx.pylibdmtx import decode

# Path to your image
image_path = "matrix.jpg"

# Read and preprocess
img = cv2.imread(image_path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Optional enhancement
enhanced = cv2.convertScaleAbs(gray, alpha=2, beta=15)

# Decode Data Matrix
decoded_objects = decode(enhanced)

if decoded_objects:
    for obj in decoded_objects:
        print("Decoded Data:", obj.data.decode('utf-8'))
else:
    print("No Data Matrix code detected.")

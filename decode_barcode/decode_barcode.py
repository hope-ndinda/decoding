from pyzbar.pyzbar import decode
from PIL import Image

# Load the image
img = Image.open("barcode.jpg")

# Decode the barcode
decoded_objects = decode(img)

for obj in decoded_objects:
    print("Type:", obj.type)
    print("Data:", obj.data.decode("utf-8"))

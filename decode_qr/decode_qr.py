import cv2
from pyzbar.pyzbar import decode
import matplotlib.pyplot as plt

# Load the image
image_path = 'qr.jpg'
img = cv2.imread(image_path)

# Decode the QR code(s)
decoded_objects = decode(img)

# Print and show the decoded data
for obj in decoded_objects:
    print(f"Decoded data: {obj.data.decode('utf-8')}")

    # Draw a rectangle around the QR code
    rect_points = obj.polygon
    if len(rect_points) == 4:
        pts = cv2.polylines(img, [np.array(rect_points, dtype=np.int32)], isClosed=True, color=(0, 255, 0), thickness=2)

# Convert the image from BGR to RGB (OpenCV uses BGR)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Show the image with the QR code highlighted
plt.imshow(img_rgb)
plt.axis('off')
plt.show()

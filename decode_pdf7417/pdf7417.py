from pdf417decoder import PDF417Decoder
from PIL import Image, ImageEnhance
import string

img = Image.open("pdf.jpg")
img = ImageEnhance.Contrast(img).enhance(1.8)
img = ImageEnhance.Sharpness(img).enhance(2.0)

decoder = PDF417Decoder(img)
decoder.decode()

for i, barcode_data in enumerate(decoder.barcodes_data):
    print(f"\n--- Cleaned Barcode {i + 1} ---")
    
    cleaned = ''.join(chr(b) for b in barcode_data if chr(b) in string.printable)
    print(cleaned)

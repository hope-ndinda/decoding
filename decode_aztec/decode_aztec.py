import cv2
from pyzxing import BarCodeReader

def decode_aztec_zxing(image_path):
    reader = BarCodeReader()
    result = reader.decode(image_path)
    
    if not result:
        print("No Aztec codes found with ZXing.")
    else:
        for res in result:
            print("Type:", res.get("format", "Unknown"))
            print("Decoded Data:", res.get("raw", "No data"))

if __name__ == "__main__":
    decode_aztec_zxing("aztec.jpg")

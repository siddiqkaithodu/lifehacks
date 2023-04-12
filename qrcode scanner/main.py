Scan any Qrcode and extract the data using the script below. This killer script uses the Pyzbar module which is popular for creating and decoding QR codes. This script is very handy for decoding multiple Qrcodes or for use in your project.

# QrCode Scanner
# pip install pyzbar
# pip install opencv-python
import cv2 as opencv
from pyzbar.pyzbar import decode
img = opencv.imread('qrcode.png')
decodedObj = decode(img)
for obj in decodedObj:
    print('Type : ', obj.type)
    print('Data : ', obj.data,'\n')

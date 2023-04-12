# Image Compressor
# pip install opencv-python
import cv2
from cv2 import imwrite
def Image_Compressor(img_file):
    img = cv2.imread(img_file)
    imwrite('compressed.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 0])
    print('Image Compressed...')
Image_Compressor('test.jpg')

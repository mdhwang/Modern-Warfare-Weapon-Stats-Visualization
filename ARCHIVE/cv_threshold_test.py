import pytesseract as tess
from PIL import Image
import cv2 as cv

import numpy as np
from matplotlib import pyplot as plt


# img = Image.open('test.png')

img = cv.imread('mono.png',0)
ret,thresh1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
ret,thresh2 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV) # GOOD
ret,thresh3 = cv.threshold(img,127,255,cv.THRESH_TRUNC)
ret,thresh4 = cv.threshold(img,127,255,cv.THRESH_TOZERO) # GOOD
ret,thresh5 = cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)

images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
for each in images:
    print('--------')
    print(tess.image_to_string(each))
    print('--------')

# print(text)
# text = tess.image_to_string(thresh1)

# titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
# for i in range(6):
#     plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
#     plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])
# plt.show()

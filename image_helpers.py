import cv2

from os import listdir
from os.path import isfile, join

from color_classifier import *

import csv

def halfsize(img):
    y,x = img.shape
    half = int(x/2)
    cropped = img[0:y,0:half]
    # cv2.imshow('test',cropped)
    # cv2.waitKey(0)  
    # cv2.destroyAllWindows() 
    return cropped

def muzzle(img):
    pass

def barrel(img):
    pass

def laser(img):
    pass

def optic(img):
    pass

def stock(img):
    pass

def perk(img):
    pass

def grip(img):
    pass

def ammunition(img):
    pass

def underbarrel(img):
    pass

img = cv2.imread('aug.png',0)
cropped = halfsize(img)
cv2.imwrite('aug.png',cropped)
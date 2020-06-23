import cv2

from os import listdir
from os.path import isfile, join

from color_classifier import *

import csv


coords = {
    'stats_table' : (195,490,831,970),
    
}

def halfsize(img):
    y,x = img.shape
    half = int(x/2)
    cropped = img[0:y,0:half]
    # cv2.imshow('test',cropped)
    # cv2.waitKey(0)  
    # cv2.destroyAllWindows() 
    return cropped

def stats_table(img):
    x0,x1,y0,y1 = coords['stats_table']
    stats_window = img[y0:y1,x0:x1]
    return stats_window

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
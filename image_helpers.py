import cv2

from os import listdir
from os.path import isfile, join

from color_classifier import *

import csv


coords = {
    'stats_table' : (195,490,831,970),
    
}

def halfsize(img):
    y,x,z = img.shape
    half = int(x/2)
    cropped = img[0:y,0:half,0:z]
    return cropped

def get_stats(img):
    x0,x1,y0,y1 = coords['stats_table']
    stats_window = img[y0:y1,x0:x1]

    stat_lines = []    
    slice_size = round(img.shape[0]/6)
    for i in range(0,6):
        start = i * slice_size
        end = start + slice_size
        stat = img[start:end,:]
        stat_lines.append(stat)

    attachment_stats = []
    for i,each in enumerate(stat_lines):
        mid = round(each.shape[0]/2)
        arr = each[mid,:]
        attachment_stats.append(color_classifier(arr,category))
    
    row = [weapon, category, name] + attachment_stats
    rows.append(row)
    return attachment_name, attachment_stats


import cv2

from os import listdir
from os.path import isfile, join

from color_classifier import *

import csv

# weapon = input("What Gun? : ")
weapon = "M4A1"
mypath = 'data/images/{}'.format(weapon)
files = [f for f in listdir(mypath) if isfile(join(mypath, f))]

x0,x1,y0,y1 = (195,490,831,970)
categories = ['Accuracy','Damage','Range','Fire Rate','Mobility','Control']
types = ['MUZZLE','BARREL','UNDERBARREL','GRIP','STOCK','LASER','BASE']
csv_header = ['Weapon','Category','Attachment','Accuracy','Damage','Range','Fire Rate','Mobility','Control']

rows = []

for attachment in files:
    category = attachment.split('-')[1]
    name = '_'.join(attachment.split('.')[0].split('-')[2:])
    
    path = 'data/images/{}/{}'.format(weapon,attachment)
    img = cv2.imread(path,0)
    crop = img[y0:y1,x0:x1]
    crop_path = 'images/cropped/{}/{}'.format(weapon,attachment)
    cv2.imwrite(crop_path, crop) 
    
    stat_lines = []    
    slice_size = round(crop.shape[0]/6)
    for i in range(0,6):
        start = i * slice_size
        end = start + slice_size
        stat = crop[start:end,:]
        stat_lines.append(stat)

    attachment_stats = []
    for i,each in enumerate(stat_lines):
        mid = round(each.shape[0]/2)
        arr = each[mid,:]
        attachment_stats.append(color_classifier(arr,category))
    
    row = [weapon,category,name] + attachment_stats
    rows.append(row)


with open("attachment_data.csv","w") as file:
    writer = csv.writer(file)
    writer.writerow(csv_header)
    for row in rows:
        writer.writerow(row)

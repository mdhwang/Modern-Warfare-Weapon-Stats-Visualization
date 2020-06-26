import cv2

from os import listdir

from color_classifier import *

import pytesseract as tess

import csv


coords = {
    'stats_table' : (195, 490, 831, 970),
    'Name' : (1550, 1870, 175, 205),
}


categories = ['Accuracy','Damage','Range','Fire Rate','Mobility','Control']

csv_header = ['Class', 'Weapon','Category','Attachment','Accuracy','Damage','Range','Fire Rate','Mobility','Control']


q = input('Will parse images from Guns folder - Continue? y/n? : ')
if q == "y":
    print("Running Program")
    count = 0
    rows = []
    classes = listdir('data/Guns/')
    if '.DS_Store' in classes:
        classes.remove(".DS_Store")
    for wep_class in classes:
        guns = listdir('data/Guns/{}'.format(wep_class))
        if '.DS_Store' in guns:
            guns.remove(".DS_Store")
        for gun in guns:
            categories = listdir('data/Guns/{}/{}'.format(wep_class, gun))
            if '.DS_Store' in categories:
                categories.remove(".DS_Store")
            for category in categories:
                attachments = listdir('data/Guns/{}/{}/{}'.format(wep_class, gun, category))
                if '.DS_Store' in attachments:
                    attachments.remove('.DS_Store')
                for attachment in attachments:
                    path = 'data/Guns/{}/{}/{}/{}'.format(wep_class, gun, category, attachment)
                    img = cv2.imread(path, 0)
                    
                    x0,x1,y0,y1 = coords['stats_table']
                    stats_window = img[y0:y1,x0:x1]
                    
                    x0,x1,y0,y1 = coords['Name']
                    attachment_window = img[y0:y1,x0:x1]
                    att_name = tess.image_to_string(attachment_window)
                    
                    stat_lines = []    
                    slice_size = round(stats_window.shape[0]/6)
                    for i in range(0,6):
                        start = i * slice_size
                        end = start + slice_size
                        stat = stats_window[start:end,:]
                        stat_lines.append(stat)
                    
                    attachment_stats = []
                    for i,each in enumerate(stat_lines):
                        mid = round(each.shape[0]/2)
                        arr = each[mid,:]
                        attachment_stats.append(color_classifier(arr,category))
                    
                    row = [wep_class, gun, category, att_name] + attachment_stats
                    rows.append(row)
                    print("Processed {} images".format(count))
                    count += 1

                    
    with open("attachment_data.csv","w") as file:
        writer = csv.writer(file)
        writer.writerow(csv_header)
        for row in rows:
            writer.writerow(row)
    
    print("Completed")
else:
    print("Skipped")
    
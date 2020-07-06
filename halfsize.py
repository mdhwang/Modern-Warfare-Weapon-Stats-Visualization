import cv2

from os import listdir

from image_helpers import *


q = input('Will overwrite screenshots from Guns folder with cropped and BW versions - Continue? y/n? : ')
if q == "y":
    print("Running Program")
    count = 0
    classes = listdir('data/Guns_Full/')
    if '.DS_Store' in classes:
        classes.remove(".DS_Store")
    for wep_class in classes:
        guns = listdir('data/Guns_Full/{}'.format(wep_class))
        if '.DS_Store' in guns:
            guns.remove(".DS_Store")
        for gun in guns:
            categories = listdir('data/Guns_Full/{}/{}'.format(wep_class, gun))
            if '.DS_Store' in categories:
                categories.remove(".DS_Store")
            for category in categories:
                attachments = listdir('data/Guns_Full/{}/{}/{}'.format(wep_class, gun, category))
                if '.DS_Store' in attachments:
                    attachments.remove('.DS_Store')
                for attachment in attachments:
                    path = 'data/Guns_Full/{}/{}/{}/{}'.format(wep_class, gun, category, attachment)
                    img = cv2.imread(path)
                    cropped = halfsize(img)
                    cv2.imwrite(path,cropped)
                    print("Processed {} images".format(count))
                    count += 1
    print("Completed")
else:
    print("Skipped")
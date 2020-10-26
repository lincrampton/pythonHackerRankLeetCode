''' 
Iterate through each file in the folder
For each file:
    Rotate the image 90° clockwise
    Resize the image from 192x192 to 128x128
    Save the image to a new folder in .jpeg format
'''

#!/usr/bin/env python3

import os
from PIL import Image

path = os.path.expanduser('~') 
ath = os.path.expanduser('~') + '/images/'
for img in os.listdir(path):
    if '48dp' in img and '.' not in img[0]:
        image_in = image_path + img
        image_save_file = "/opt/icons/" + image + ".jpeg"
        image = Image.open(image_in)
        image.rotate(90).resize((128,128)).convert('RGB').save(image_save)
        image.close()


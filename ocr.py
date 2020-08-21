import numpy as np
import cv2
from PIL import Image 
import pytesseract 
import sys 
from pdf2image import convert_from_path 
import sys
import os
import random

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pages = convert_from_path('Flyer BAR 2020.pdf', 500)

image_counter = 1
for page in pages:
    filename = "page_"+str(image_counter)+".jpg"
    page.save(filename, 'JPEG')
    image_counter = image_counter + 1
        
    ''' 
    Part #2 - Recognizing text from the images using OCR 
    '''
    filelimit = image_counter-1

    basepath = os.path.dirname(__file__)
    file_path2 = os.path.join(
        basepath, 'outputs', "output"+str(random.randint(1, 
                                                         100000))+".txt")
         
    f = open(file_path2, "a") 

    for i in range(1, filelimit + 1): 

        filename = "page_"+str(i)+".jpg"
 
        text = str(((pytesseract.image_to_string(Image.open(
            filename))))) 
      
        f.write(text) 
    print(" text extracted is saved in ouput  folder")
 
    f.close()
    


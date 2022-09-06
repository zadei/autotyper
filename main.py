from PIL import ImageGrab, Image
from pytesseract import pytesseract
from pynput.keyboard import Key, Controller
from pathlib import Path
import pyautogui
import time
import os.path
import os
import random
random.seed(69)
keyboard = Controller()

# pyautogui.click(337, 479)
# time.sleep(1)
# #create new screenshot of text box
# #pic = ImageGrab.grab(bbox=(342, 473, 1325, 635)) # coordinates of word box (monitor res 1680x1050)
# #pic.save("ss.png")

#path to image
path_to_image = 'ss.png'

#display image (testing)
img = Image.open(path_to_image)
# input("press enter if the screenshot was OK")

#path to tesseract.exe
path_to_tesseract = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

#point tesseract_cmd module to tesseract.exe
pytesseract.tesseract_cmd = path_to_tesseract

#extract text from image
text = pytesseract.image_to_string(img)
#filter out \n
text = text.replace('\n', ' ')
print(text)
#split into character array

textarrchar = list(text)

#press to focus on monkeytype window
pyautogui.click(337, 479)
time.sleep(1)
#loop through all characters in array and type them
for i in range(len(textarrchar)):
    keyboard.press(textarrchar[i])
    keyboard.release(textarrchar[i])
    time.sleep(random.uniform(0.06, 0.078))
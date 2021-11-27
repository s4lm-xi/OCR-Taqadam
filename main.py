import pytesseract
import subprocess
import time
import pyautogui as gui
import pyttsx3
import cv2

subprocess.Popen(r'C:\Users\salman\Documents\Processing\DigitRecognizer\Optical Character Recognition\ocr\ocr.pde', shell=True)
time.sleep(10)

runCoords = [399, 161]
#drawing window size
x1 = 363-30
y1 = 186-20

x2 = 1003+30
y2 = 572+20

gui.click(runCoords[0], runCoords[1])

time.sleep(5)

engine = pyttsx3.init()
engine.setProperty('rate', 120)
engine.say("Start drawing")
engine.runAndWait()

time.sleep(10)

engine.setProperty('rate', 120)
engine.say("Stop Drawing!")
engine.runAndWait()

time.sleep(2)

gui.screenshot('screenshots/1.jpg')

img = cv2.imread('screenshots/1.jpg')

roi = img[y1:y1+y2-y1, x1:x1+x2-x1]

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
text = pytesseract.image_to_string(roi)

engine.setProperty('rate', 120)
engine.say("You wrote!")
engine.runAndWait()

time.sleep(3)

engine.setProperty('rate', 120)
engine.say(text)
engine.runAndWait()

print(text)

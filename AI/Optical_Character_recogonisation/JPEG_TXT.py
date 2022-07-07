import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# read image
im = cv2.imread('./R')
# configurations
config = ('-l eng --oem 3 --psm 4')
# pytesseract
text = pytesseract.image_to_string(im, config=config)
# print(text)
# text = text.split('\n')
print(text)
with open('resume.txt', 'w') as f:
    f.write(text)
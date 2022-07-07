# text recognition
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# read image
im = cv2.imread('R.jpg')
# configurations
# config = ('-l eng --oem 1 --psm 3')
# pytesseract
text = pytesseract.image_to_string(im)
# print text
# text = text.split('\n')
print(text)
# with open('ocr1.txt', 'w') as f:
#     f.write(text)
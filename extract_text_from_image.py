from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"/home/test/.local/lib/python3.9/site-packages/pytesseract/pytesseract.py"

image = Image.open("Brad-Pitt-and-Jennifer-Aniston.jpg")

text = pytesseract.image_to_string(image, lang="en")

print(text)

#/usr/lib/python3/dist-packages
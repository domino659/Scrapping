import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Tesseract-OCR\tesseract.exe'


def resolve():
    print("Reasempling the Image")
    return pytesseract.image_to_string('img/captcha_screenshot.png')

print(resolve())

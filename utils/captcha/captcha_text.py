import os
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from variable import PATH_TESSERACT


def detect_capcha(driver):
    sleep(2)
    try:
        captcha = driver.find_element_by_id("captchaForm")
        if captcha:
            {
                capcha(driver)
            }
    except NoSuchElementException:
        pass


def capcha(driver):
    # Take screen of the captcha and save it.
    path = 'img'
    # Create folder for img
    isExist = os.path.exists(path)
    if not isExist:
        os.makedirs(path)

    driver.find_element_by_id("captchaImg").screenshot(
        'img/captcha_screenshot.png')
    # Solve the captchat using Maching learning
    captcha_text = resolve()
    captcha = driver.find_element_by_id("captchaChars")
    captcha.send_keys(captcha_text)
    # If fail and captcha not solved will try again
    detect_capcha(driver)


def resolve():
    import pytesseract

    pytesseract.pytesseract.tesseract_cmd = PATH_TESSERACT
    result = pytesseract.image_to_string('img/captcha_screenshot.png')

    return result

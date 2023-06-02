from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()

try:
    browser.get("http://suninjuly.github.io/alert_accept.html")
    submit = browser.find_element(By.CLASS_NAME, "btn-primary")
    submit.click()
    confirmation = browser.switch_to.alert
    confirmation.accept()
    value = browser.find_element(By.ID, "input_value")
    x = int(value.text)
    y = calc(x)
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(str(y))
    butt = browser.find_element(By.CLASS_NAME, "btn-primary")
    butt.click()

finally:
    time.sleep(15)
    browser.quit()

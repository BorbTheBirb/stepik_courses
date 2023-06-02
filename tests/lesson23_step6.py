from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()

try:
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    button = browser.find_element(By.CLASS_NAME, "trollface")
    button.click()
    browser.switch_to.window(browser.window_handles[1])  # вызываем лист вкладок и переходим на вторую
    x = browser.find_element(By.ID, "input_value")
    y = str(calc(int(x.text)))
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)
    butt = browser.find_element(By.CLASS_NAME, "btn-primary")
    butt.click()
    result = browser.switch_to.alert.text
    print(result)

finally:
    browser.quit()

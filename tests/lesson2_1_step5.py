from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()

try:
    browser.get("http://suninjuly.github.io/get_attribute.html")
    value = browser.find_element(By.ID, 'treasure')
    x = value.get_attribute('valuex')
    y = calc(x)
    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(y)
    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    checkbox.click()
    radio = browser.find_element(By.ID, 'robotsRule')
    radio.click()
    submit = browser.find_element(By.CLASS_NAME, 'btn-default')
    submit.click()

finally:
    time.sleep(15)
    browser.quit()

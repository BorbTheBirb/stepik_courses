from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()

try:
    browser.get("http://suninjuly.github.io/execute_script.html")
    value = browser.find_element(By.ID, 'input_value')
    x = value.text
    y = calc(x)
    button = browser.find_element(By.TAG_NAME, "button")
    browser.find_element(By.CLASS_NAME, "bd-footer")
    browser.execute_script("document.querySelector(\".bd-footer\").style.display = \"none\";")
    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(y)
    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    checkbox.click()
    radio = browser.find_element(By.ID, 'robotsRule')
    radio.click()
    submit = browser.find_element(By.CLASS_NAME, 'btn-primary')
    submit.click()

finally:
    time.sleep(15)
    browser.quit()

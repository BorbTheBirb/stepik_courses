from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


browser = webdriver.Chrome()

try:
    browser.get("http://suninjuly.github.io/selects1.html")
    value1 = browser.find_element(By.ID, 'num1')
    value2 = browser.find_element(By.ID, 'num2')
    x = int(value1.text) + int(value2.text)
    answers = Select(browser.find_element(By.CLASS_NAME, 'custom-select'))
    answers.select_by_value(str(x))
    submit = browser.find_element(By.CLASS_NAME, 'btn-default')
    submit.click()

finally:
    time.sleep(10)
    browser.quit()

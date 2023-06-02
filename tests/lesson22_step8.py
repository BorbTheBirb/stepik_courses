from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()

try:
    browser.get("http://suninjuly.github.io/file_input.html")
    fname = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
    fname.send_keys("scrunko")
    lname = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
    lname.send_keys("bunko")
    email = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
    email.send_keys("hunko@tun.ko")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'butts.txt')  # добавляем к этому пути имя файла
    file_field = browser.find_element(By.ID, "file")
    file_field.send_keys(file_path)
    submit = browser.find_element(By.CLASS_NAME, 'btn-primary')
    submit.click()

finally:
    time.sleep(15)
    browser.quit()

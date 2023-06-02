from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math, time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()

try:
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    text = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
    btn = browser.find_element(By.ID, "book")
    btn.click()
    heck = browser.find_element(By.ID, 'input_value').text
    y = calc(heck)
    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(y)
    ansbutton = browser.find_element(By.ID, 'solve')
    ansbutton.click()
    result = browser.switch_to.alert.text
    print(result)
    time.sleep(10)

finally:
    browser.quit()
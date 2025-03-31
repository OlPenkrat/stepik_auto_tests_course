from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
   return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5) # говорим WebDriver ждать все элементы в течение 5 секунд
    browser.get(link)

    text = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
    button = browser.find_element(By.ID, "book")
    button.click()
    
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)
    # print(y)
 
    input = browser.find_element(By.CSS_SELECTOR, '#answer')
    # browser.execute_script("return arguments[0].scrollIntoView(true);", input)
    input.send_keys(y)

    button = browser.find_element(By.ID, "solve").click()


finally:
    time.sleep(7)
    browser.quit()

    # add to new repozitory
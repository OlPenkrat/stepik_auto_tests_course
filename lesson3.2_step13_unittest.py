from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"


class TestRegistration(unittest.TestCase):
    def test_fill_form(self, link):
        browser = webdriver.Chrome()
        browser.get(link)
  
        input1 = browser.find_element(By.CSS_SELECTOR, 'div.first_block  .first')
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, 'div.first_block  .second')
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, 'div.first_block  .third')
        input3.send_keys("Smolensk@gmai.com")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        return welcome_text

    def test_regestration1(self):
        filled_form = self.test_fill_form(link1)
        self.assertIn("successfully", filled_form.welcome_text, "Wrong Welcome text")
    
    def test_registration2(self):
        filled_form = self.test_fill_form(link2)
        self.assertIn("successfully", filled_form.welcome_text, "Wrong Welcome text")  
        
if __name__ == "__main__":
    unittest.main()
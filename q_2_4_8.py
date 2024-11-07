from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
          return str(math.log(abs(12*math.sin(int(x)))))

try:
    
    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    
    browser.get(link)

    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), text_='100'))
    browser.find_element(By.ID, 'book').click()
    
    x = browser.find_element(By.ID, 'input_value')
    y = x.text
    z = calc(y)

    browser.find_element(By.ID, 'answer').send_keys(z)
    
    browser.find_element(By.CSS_SELECTOR, '#solve').click()

finally:
    time.sleep(2)
    browser.quit()
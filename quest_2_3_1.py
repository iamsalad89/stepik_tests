from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
          return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = 'https://suninjuly.github.io/alert_accept.html'
browser.get(link)

first_button = browser.find_element(By.CLASS_NAME, 'btn')
first_button.click()

#time.sleep(1)

#alert = browser.switch_to.alert
#alert.accept()


x = browser.find_element(By.ID, 'input_value')
y = x.text

z = calc(y)

fieldd = browser.find_element(By.ID, 'answer')
fieldd.send_keys(z)

button = browser.find_element(By.CLASS_NAME, 'btn')
button.click()


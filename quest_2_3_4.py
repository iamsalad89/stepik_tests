from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
          return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = 'https://suninjuly.github.io/redirect_accept.html'

browser.get(link)

troll_button = browser.find_element(By.CLASS_NAME, 'trollface')
troll_button.click()

time.sleep(2)

new_window = browser.window_handles[1]

browser.switch_to.window(new_window)

x = browser.find_element(By.ID, 'input_value')
y = x.text
z = calc(y)

field = browser.find_element(By.ID, 'answer')
field.send_keys(z)

button = browser.find_element(By.CLASS_NAME, 'btn-primary')
button.click()


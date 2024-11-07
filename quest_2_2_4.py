from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
          return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "https://suninjuly.github.io/execute_script.html"
browser.get(link)

perem = browser.find_element(By.ID, 'input_value')
x = perem.text
z = calc(x)

puk = browser.find_element(By.ID, 'answer')
browser.execute_script("return arguments[0].scrollIntoView(true);", puk)
puk.send_keys(z)

robot = browser.find_element(By.ID, 'robotCheckbox')
robot.click()

robot_rule = browser.find_element(By.ID, 'robotsRule')
robot_rule.click()

button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
button.click()

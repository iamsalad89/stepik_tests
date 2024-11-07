from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
          return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "https://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    treasure = browser.find_element(By.ID, 'treasure')
    treasure_attr = treasure.get_attribute('valuex')
    x = treasure_attr
    y = calc(x)

    answer = browser.find_element(By.CSS_SELECTOR, '#answer')
    answer.send_keys(y)   

    im_rob = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    im_rob.click()

    im_rob_radi = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    im_rob_radi.click()

    button = browser.find_element(By.CSS_SELECTOR, '.btn')
    button.click()
    
    assert "Congratulations! You have successfully registered!"

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

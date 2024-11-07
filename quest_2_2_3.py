from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def res(x, y):
    puk = int(x) + int(y)
    return str(puk)

try:
    link = 'https://suninjuly.github.io/selects2.html'
    browser = webdriver.Chrome()
    browser.get(link)

    first = browser.find_element(By.CSS_SELECTOR, '#num1')
    x = first.text
    second = browser.find_element(By.CSS_SELECTOR, '#num2')
    y = second.text
    z = res(x, y)

    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    select.select_by_value(z)

    sub = browser.find_element(By.CSS_SELECTOR, '.btn.btn-default')
    sub.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()




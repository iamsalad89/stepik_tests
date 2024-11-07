from selenium import webdriver
from selenium.webdriver.common.by import By
import os

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/file_input.html'
browser.get(link)

first_name = browser.find_element(By.NAME, "firstname")
last_name = browser.find_element(By.NAME, "lastname")
email = browser.find_element(By.NAME, "email")

cred = [first_name, last_name, email]

for selectors in cred:
    selectors.send_keys('ger')

file_upload = browser.find_element(By.ID, 'file')
file_upload.send_keys(file_path)

button = browser.find_element(By.CLASS_NAME, 'btn')
button.click()


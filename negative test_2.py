from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service()
driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

login_standart_user = "standard_use"
password_all = "secret_sauce"

user_name = driver.find_element(By. XPATH, "//input[@class = 'input_error form_input' and @placeholder = 'Username']")  #xPath
user_name.send_keys(login_standart_user)
print(f"Input Login")
password = driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password_all)  #CSS.SELECTOR
print(f"Input Password")
button_login = driver.find_element(By.XPATH, "//input[@type = 'submit']").click()
print(f"Click Login Button")
"""Проводим негативный тест. Логин пишем не правльно"""
warring_text = driver.find_element(By.XPATH, "//h3[@data-test = 'error']")  #локатор ошибки что не правльный логин
value_warring_text = warring_text.text
assert value_warring_text == "Epic sadface: Username and password do not match any user in this service"    #копируем текст ошибки чтобы сравнить
print(f"Good Test")

#driver.refresh()  - #обновление страницы

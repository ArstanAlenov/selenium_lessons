import time

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

login_standart_user = "standard_user"
password_all = "secret_sauce"

user_name = driver.find_element(By. XPATH, "//input[@class = 'input_error form_input' and @placeholder = 'Username']")  #xPath
user_name.send_keys(login_standart_user)
print(f"Input Login")
password = driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password_all)  #CSS.SELECTOR
print(f"Input Password")
button_login = driver.find_element(By.XPATH, "//input[@type = 'submit']").click()
print(f"Click Login Button")

menu = driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']").click() #находим кнопку которая содержит скрытое меню (выпадающий список)
print(f"click menu button")
time.sleep(3)
link_about = driver.find_element(By.XPATH, "//a[@id='about_sidebar_link']").click() #жмем на кнопку из выпадающего списка
print(f"click link button")

driver.back() #перемещаемся назад (стрелкой)
print("Go Back")
time.sleep(5)
driver.forward() #перемещаемся вперед (стрелкой)
print("Go forward")
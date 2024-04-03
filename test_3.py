import time

from selenium import webdriver
from selenium.webdriver import Keys
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

#"""Имитация нажатия клавиш""""

user_name = driver.find_element(By. XPATH, "//input[@class = 'input_error form_input' and @placeholder = 'Username']")  #xPath
user_name.send_keys(login_standart_user)
print(f"Input Login")
time.sleep(5)
user_name.send_keys(Keys. BACKSPACE) #стирает последний символ
time.sleep(3)
user_name.send_keys(Keys. BACKSPACE) #для удаления второго символа просто копируем строчку кода
time.sleep(3)
user_name.send_keys("er") #добавили снова два наших удаленных символа
#password = driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password_all)  #CSS.SELECTOR
#print(f"Input Password")
#button_login = driver.find_element(By.XPATH, "//input[@type = 'submit']").click()
#print(f"Click Login Button")

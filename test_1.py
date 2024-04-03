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

"""Проверяем что мы точно авторизовались по слову на странице"""
#text_products = driver.find_element(By.XPATH, "//span[@class = 'title']")
#value_text_products = text_products.text
#print(value_text_products)
#assert value_text_products == "Products"
#print(f"GOOD")

"""Проверяем что мы точно авторизовались по url"""
url = "https://www.saucedemo.com/inventory.html"
get_url = driver.current_url
print(get_url)
assert url == get_url
print(f"GOOD url")
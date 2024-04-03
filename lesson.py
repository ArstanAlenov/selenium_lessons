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
#user_name = driver.find_element(By. ID, "user-name")    #ID
#user_name = driver.find_element(By. NAME, "user-name")  #NAME
user_name = driver.find_element(By. XPATH, "//input[@class = 'input_error form_input' and @placeholder = 'Username']")  #xPath
user_name.send_keys("standard_user")
password = driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")  #CSS.SELECTOR
button_login = driver.find_element(By.XPATH, "//input[@type = 'submit']").click()





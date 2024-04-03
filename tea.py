import time
import datetime

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service()
driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://slon.store/'
driver.get(base_url)
driver.maximize_window()


email_name = "autotestingqa@mail.ru"
password_in = "SeleniuM1985"

time.sleep(5)

to_come_in_main_page = driver.find_element(By.XPATH, "//a[@class='login-link']").click()
time.sleep(5)

user_name = driver.find_element(By.XPATH, "//input[@id='input-email']")
user_name.send_keys(email_name)
time.sleep(3)

password = driver.find_element(By.XPATH, "//input[@id='input-password']")
password.send_keys(password_in)
time.sleep(3)

to_come_in = driver.find_element(By.XPATH, "//input[@type='submit']").click()
time.sleep(3)

main_button_menu = driver.find_element(By.XPATH, "//li[@class='burger']").click()
time.sleep(5)

product_choice = driver.find_element(By.XPATH, "//a[@href='/kofe']").click()
time.sleep(5)

product = driver.find_element(By.XPATH, "(//a[@href='http://slon.store/kofe-v-zernah-kuba-serrano'])[2]").click()
time.sleep(5)

weight_product = driver.find_element(By.XPATH, "//label[@class='active']").click()
time.sleep(5)




















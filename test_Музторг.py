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
base_url = 'https://www.muztorg.ru/'
driver.get(base_url)
driver.maximize_window()


email_name = "autotestingqa@mail.ru"
password_in = "SeleniuM1985"

time.sleep(5)

to_come_in_main_page = driver.find_element(By.XPATH, "(//a[@href='/site/get-login-form'])[2]").click()
time.sleep(5)

to_come_in_pass = driver.find_element(By.XPATH, "//a[@class='js-login-way']").click()
time.sleep(3)

email = driver.find_element(By.XPATH, "//input[@name='LoginForm[login]']")
email.send_keys(email_name)
time.sleep(3)

password = driver.find_element(By.XPATH, "//input[@type='password']")
password.send_keys(password_in)
time.sleep(3)

to_come_in = driver.find_element(By.XPATH, "//button[@id='login-by-pass_submit-btn']").click()



















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
base_url = 'https://demoqa.com/date-picker'
driver.get(base_url)
driver.maximize_window()

new_date = driver.find_element(By.XPATH, "//input[@id='datePickerMonthYearInput']")
new_date.send_keys(Keys.BACKSPACE*10)
date = datetime.datetime.today() + datetime.timedelta(days=10)
new_date.send_keys(str(date))
new_date.send_keys(Keys.RETURN)


















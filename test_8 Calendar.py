import time

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
#new_date.clear()
new_date.send_keys(Keys.BACKSPACE*10)

time.sleep(5)
new_date.send_keys("08/15/2020")
time.sleep(5)
new_date.send_keys(Keys.RETURN)
new_date.click()
time.sleep(3)
date_24 = driver.find_element(By.XPATH, "//div[@class='react-datepicker__day react-datepicker__day--024']").click()






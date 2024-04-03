import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service()
driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://www.moex.com/'
driver.get(base_url)
driver.maximize_window()

time.sleep(3)
catalog = driver.find_element(By.XPATH, "//div[@class='scroll-button scroll-button_right invisible']").click()




#div[@class = 'header-nav__mobile-menu-button']
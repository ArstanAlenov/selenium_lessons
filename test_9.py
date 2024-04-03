from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service()
driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://demoqa.com/dynamic-properties'
driver.get(base_url)
driver.maximize_window()

# driver.implicitly_wait(10) #неявное ожидание

# visible_button = driver.find_element(By.XPATH, "//button[@id='visibleAfter']").click()

visible_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable(By.XPATH, "//button[@id='visibleAfter']"))) #явное ожидание
visible_button.click()
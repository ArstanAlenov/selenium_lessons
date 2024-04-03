from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service()
driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://demoqa.com/buttons'
driver.get(base_url)
driver.maximize_window()

#нажатие двойного клика мыши
action = ActionChains(driver)
double = driver.find_element(By.XPATH, "//button[@id='doubleClickBtn']")
action.double_click(double).perform()

#нажатие пр.кн. мыши
right_click = driver.find_element(By.XPATH, "//button[@id='rightClickBtn']")
action.context_click(right_click).perform()


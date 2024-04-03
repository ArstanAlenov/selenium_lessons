from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service()
driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://demoqa.com/checkbox'
driver.get(base_url)
driver.maximize_window()

check_box_strelka = driver.find_element(By.XPATH, "//button[@aria-label='Toggle']")
check_box_strelka.click()
check_box = driver.find_element(By.XPATH, "(//span[@class='rct-checkbox'])[4]").click()

check_box_text = driver.find_element(By.XPATH, "//span[contains(text(), 'downloads')]")
value_check_box_text = check_box_text.text
print(value_check_box_text)
assert value_check_box_text == "downloads"
print("Good")




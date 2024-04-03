import time
import datetime
from argparse import Action

from selenium import webdriver
from selenium.webdriver import ActionChains
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

#Скролл сайта

#driver.execute_script("window.scrollTo(0, 500)") - перемещение вниз

#наводимся на элемент и делаем скиншот
action = ActionChains(driver)
twitter_button = driver.find_element(By.XPATH, "//a[@href='https://twitter.com/saucelabs']")
action.move_to_element(twitter_button).perform()

time.sleep(5)

now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S") #Вывод даты  и времени в настоящий момент
name_screenshot = 'creenshot.png ' + now_date + '.png'
driver.save_screenshot('C:\\Users\\User.WSA34411\PycharmProjects\\Selenium_lessons\\screen\\' + name_screenshot)

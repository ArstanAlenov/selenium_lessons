from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest

from pages.login_page import Login_page



def test_buy_product():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument('--ignore-certificate-errors-spki-list')
    options.add_argument('--ignore-ssl-errors')
    g = Service('C:\\Users\\User.WSA34411\\PycharmProjects\\resource\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=g)


    login = Login_page(driver)
    login.authorization()
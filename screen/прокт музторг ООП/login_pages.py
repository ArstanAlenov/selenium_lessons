from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class Login_page(Base):

    url = 'https://www.muztorg.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators



    to_come_in_main_page = "(//a[@href='/site/get-login-form'])[2]"
    to_come_in_pass = "//a[@class='js-login-way']"
    email = "//input[@name='LoginForm[login]']"
    password = "//input[@type='password']"
    to_come_in = "//button[@id='login-by-pass_submit-btn']"

    # Getters

    def get_to_come_in_main_page(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.to_come_in_main_page)))

    def get_to_come_in_pass(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.to_come_in_pass)))

    def get_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_to_come_in(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.to_come_in)))

    #Action

    def click_to_come_in_main_page(self):
        self.get_to_come_in_main_page().click()
        print("Click to_come_in_main_page")

    def click_to_come_in_pass(self):
        self.get_to_come_in_pass().click()
        print("Click to_come_in_pass")

    def input_email(self, email):
        self.get_email().send_keys(email)
        print("Input email")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_to_come_in(self):
        self.get_to_come_in().click()
        print("Click to_come_in")


    #Method



    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.get_to_come_in_main_page()
        self.get_to_come_in_pass()
        self.input_email("autotestingqa@mail.ru")
        self.input_password("SeleniuM1985")
        self.get_to_come_in()
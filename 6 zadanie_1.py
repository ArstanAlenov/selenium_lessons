import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service('C:\\Users\\User.WSA34411\\PycharmProjects\\resource\\chromedriver.exe')
driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()

login_standart_user = "standard_user"
password_all = "secret_sauce"

user_name = driver.find_element(By. XPATH, "//input[@class = 'input_error form_input' and @placeholder = 'Username']")  #xPath
user_name.send_keys(login_standart_user)
password = driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password_all)  #CSS.SELECTOR
button_login = driver.find_element(By.XPATH, "//input[@type = 'submit']").click()

def privetstvie():
    print("Приветствую тебя в нашем интернет магазине")
    print("Выбери один из сдедующих товаров и укажи его номер:\n1 - Sauce Labs Backpack\n2 - Sauce Labs Bike Light\n3 -  Sauce Labs Bolt T-Shirt\n4 - Sauce Labs Fleece Jacket\n5 - Sauce Labs Onesi\n6 - Test.allTheThings() T-Shirt (Red)")


privetstvie()
product = input()

"""создаем функцию по заполнению поля для покупки товара""" #данная функция будет использоваться во всех шести товаров
def zapolnenie():
    f_name = driver.find_element(By.XPATH, "//input[@id='first-name']")
    f_name.send_keys("Olga")
    l_name = driver.find_element(By.XPATH, "//input[@id='last-name']")
    l_name.send_keys("Ivanova")
    zip = driver.find_element(By.XPATH, "//input[@id='postal-code']")
    zip.send_keys("123")
    contin = driver.find_element(By.XPATH, "//input[@id='continue']").click()

    
def product_1(): #всю логику по выбору и покупки товара записываем в функции
    prod_1 = driver.find_element(By.XPATH, "//div[@class='inventory_item_name'][1]")
    value_prod_1 = prod_1.text
    print(value_prod_1)

    price_prod_1 = driver.find_element(By.XPATH, "//div[@class='inventory_item_price'][1]")
    value_price_prod_1 = price_prod_1.text
    print(value_price_prod_1)

    select_prod_1 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']").click()
    print("select_prod_1")

    cart = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
    print("Enter cart")

    cart_prod_1 = driver.find_element(By.XPATH, "//div[@class='inventory_item_name'][1]")
    value_cart_prod_1 = cart_prod_1.text
    print(value_cart_prod_1)
    assert value_prod_1 == value_cart_prod_1
    print("INFO CartProd 1 Good")

    price_cart_prod_1 = driver.find_element(By.XPATH, "//div[@class='inventory_item_price'][1]")
    value_cart_price_prod_1 = price_cart_prod_1.text
    print(value_cart_price_prod_1)
    assert value_cart_price_prod_1 == value_cart_price_prod_1
    print("INFO Cart Price Prod 1 Good")

    checkout = driver.find_element(By.XPATH, "//button[@id='checkout']").click()
    print("click checkout")

    zapolnenie()

    finish_prod_1 = driver.find_element(By.XPATH, "//div[@class='inventory_item_name']")
    value_finish_prod_1 = finish_prod_1.text
    print(value_finish_prod_1)
    assert value_prod_1 == value_finish_prod_1
    print("INFO finishProd 1 Good")

    price_finish_prod_1 = driver.find_element(By.XPATH, "//div[@class='inventory_item_price']")
    value_finish_price_prod_1 = price_finish_prod_1.text
    print(value_finish_price_prod_1)
    assert value_cart_price_prod_1 == value_finish_price_prod_1
    print("INFO cart finish Prod 1 Good")
    time.sleep(3)
    driver.close()
    driver.quit()

def product_2():
    prod_2 = driver.find_element(By.XPATH, "//div[contains(text(), 'Bike Light')]")
    value_prod_2 = prod_2.text
    print(value_prod_2)

    price_prod_2 = driver.find_element(By.XPATH, "(//div[@class='inventory_item_price'])[2]")
    value_price_prod_2 = price_prod_2.text
    print(value_price_prod_2)

    select_prod_2 = driver.find_element(By.XPATH, "//button[contains(@name, 'labs-bike')]").click()
    print("select_prod_2")

    cart = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
    print("Enter cart")

    cart_prod_2 = driver.find_element(By.XPATH, "//div[contains(text(), 'Bike Light')]")
    value_cart_prod_2 = cart_prod_2.text
    print(value_cart_prod_2)
    assert value_prod_2 == value_cart_prod_2
    print("INFO CartProd 2 Good")

    price_cart_prod_2 = driver.find_element(By.XPATH, "//div[@class='inventory_item_price']")
    value_cart_price_prod_2 = price_cart_prod_2.text
    print(value_cart_price_prod_2)
    assert value_cart_price_prod_2 == value_cart_price_prod_2
    print("INFO Cart Price Prod 2 Good")

    checkout = driver.find_element(By.XPATH, "//button[@id='checkout']").click()
    print("click checkout")

    zapolnenie()

    finish_prod_2 = driver.find_element(By.XPATH, "//div[contains(text(), 'Bike Light')]")
    value_finish_prod_2 = finish_prod_2.text
    print(value_finish_prod_2)
    assert value_prod_2 == value_finish_prod_2
    print("INFO finishProd 2 Good")

    price_finish_prod_2 = driver.find_element(By.XPATH, "//div[@class='inventory_item_price']")
    value_finish_price_prod_2 = price_finish_prod_2.text
    print(value_finish_price_prod_2)
    assert value_cart_price_prod_2 == value_finish_price_prod_2
    print("INFO cart finish Prod 2 Good")
    time.sleep(3)
    driver.close()
    driver.quit()

def product_3():
    prod_3 = driver.find_element(By.XPATH, "//div[contains(text(), 'Sauce Labs Bolt T-Shirt')]")
    value_prod_3 = prod_3.text
    print(value_prod_3)

    price_prod_3 = driver.find_element(By.XPATH, "(//div[@class='inventory_item_price'])[3]")
    value_price_prod_3 = price_prod_3.text
    print(value_price_prod_3)

    select_prod_3 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']").click()
    print("select_prod_3")
    cart = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
    print("Enter cart")

    cart_prod_3 = driver.find_element(By.XPATH, "//div[contains(text(), 'Sauce Labs Bolt T-Shirt')]")
    value_cart_prod_3 = cart_prod_3.text
    print(value_cart_prod_3)
    assert value_prod_3 == value_cart_prod_3
    print("INFO CartProd 3 Good")

    price_cart_prod_3 = driver.find_element(By.XPATH, "//div[@class='inventory_item_price']")
    value_cart_price_prod_3 = price_cart_prod_3.text
    print(value_cart_price_prod_3)
    assert value_cart_price_prod_3 == value_cart_price_prod_3
    print("INFO Cart Price Product 3 Good")

    checkout = driver.find_element(By.XPATH, "//button[@id='checkout']").click()
    print("click checkout")

    zapolnenie()

    finish_prod_3 = driver.find_element(By.XPATH, "//div[contains(text(), 'Sauce Labs Bolt T-Shirt')]")
    value_finish_prod_3 = finish_prod_3.text
    print(value_finish_prod_3)
    assert value_prod_3 == value_finish_prod_3
    print("INFO finishProd 3 Good")

    price_finish_prod_3 = driver.find_element(By.XPATH, "//div[@class='inventory_item_price']")
    value_finish_price_prod_3 = price_finish_prod_3.text
    print(value_finish_price_prod_3)
    assert value_cart_price_prod_3 == value_finish_price_prod_3
    print("INFO cart finish Prod 3 Good")
    time.sleep(3)
    driver.close()
    driver.quit()

def product_4():
    prod_4 = driver.find_element(By.XPATH, "//div[contains(text(), 'Fleece')]")
    value_prod_4 = prod_4.text
    print(value_prod_4)

    price_prod_4 = driver.find_element(By.XPATH, "(//div[@class='inventory_item_price'])[4]")
    value_price_prod_4 = price_prod_4.text
    print(value_price_prod_4)

    select_prod_4 = driver.find_element(By.XPATH, "//button[contains(@id, 'fleece')]").click()
    print("select_prod_4")
    cart = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
    print("Enter cart")

    cart_prod_4 = driver.find_element(By.XPATH, "//div[contains(text(), 'Fleece')]")
    value_cart_prod_4 = cart_prod_4.text
    print(value_cart_prod_4)
    assert value_prod_4 == value_cart_prod_4
    print("INFO CartProduct 4 Good")

    price_cart_prod_4 = driver.find_element(By.XPATH, "//div[@class='inventory_item_price']")
    value_cart_price_prod_4 = price_cart_prod_4.text
    print(value_cart_price_prod_4)
    assert value_cart_price_prod_4 == value_cart_price_prod_4
    print("INFO Cart Price Product 4 Good")

    checkout = driver.find_element(By.XPATH, "//button[@id='checkout']").click()
    print("click checkout")

    zapolnenie()

    finish_prod_4 = driver.find_element(By.XPATH, "//div[contains(text(), 'Fleece')]")
    value_finish_prod_4 = finish_prod_4.text
    print(value_finish_prod_4)
    assert value_prod_4 == value_finish_prod_4
    print("INFO finishProduct 4 Good")

    price_finish_prod_4 = driver.find_element(By.XPATH, "//div[@class='inventory_item_price']")
    value_finish_price_prod_4 = price_finish_prod_4.text
    print(value_finish_price_prod_4)
    assert value_cart_price_prod_4 == value_finish_price_prod_4
    print("INFO cart finish Product 4 Good")
    time.sleep(3)
    driver.close()
    driver.quit()

def product_5():
    prod_5 = driver.find_element(By.XPATH, "//div[contains(text(), 'Onesie')]")
    value_prod_5 = prod_5.text
    print(value_prod_5)

    price_prod_5 = driver.find_element(By.XPATH, "(//div[@class='inventory_item_price'])[5]")
    value_price_prod_5 = price_prod_5.text
    print(value_price_prod_5)

    select_prod_5 = driver.find_element(By.XPATH, "//button[contains(@id, 'labs-onesie')]").click()
    print("select_prod_5")
    cart = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
    print("Enter cart")

    cart_prod_5 = driver.find_element(By.XPATH, "//div[contains(text(), 'Onesie')]")
    value_cart_prod_5 = cart_prod_5.text
    print(value_cart_prod_5)
    assert value_prod_5 == value_cart_prod_5
    print("INFO CartProduct 5 Good")

    price_cart_prod_5 = driver.find_element(By.XPATH, "//div[@class='inventory_item_price']")
    value_cart_price_prod_5 = price_cart_prod_5.text
    print(value_cart_price_prod_5)
    assert value_cart_price_prod_5 == value_cart_price_prod_5
    print("INFO Cart Price Product 5 Good")

    checkout = driver.find_element(By.XPATH, "//button[@id='checkout']").click()
    print("click checkout")

    zapolnenie()

    finish_prod_5 = driver.find_element(By.XPATH, "//div[contains(text(), 'Onesie')]")
    value_finish_prod_5 = finish_prod_5.text
    print(value_finish_prod_5)
    assert value_prod_5 == value_finish_prod_5
    print("INFO finishProduct 5 Good")

    price_finish_prod_5 = driver.find_element(By.XPATH, "//div[@class='inventory_item_price']")
    value_finish_price_prod_5 = price_finish_prod_5.text
    print(value_finish_price_prod_5)
    assert value_cart_price_prod_5 == value_finish_price_prod_5
    print("INFO cart finish Product 5 Good")
    time.sleep(3)
    driver.close()
    driver.quit()

def product_6():
    prod_6 = driver.find_element(By.XPATH, "//div[contains(text(), 'Test.allTheThings')]")
    value_prod_6 = prod_6.text
    print(value_prod_6)

    price_prod_6 = driver.find_element(By.XPATH, "(//div[@class='inventory_item_price'])[6]")
    value_price_prod_6 = price_prod_6.text
    print(value_price_prod_6)

    select_prod_6 = driver.find_element(By.XPATH, "//button[contains(@id, '.allthethings')]").click()
    print("select_prod_6")
    cart = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
    print("Enter cart")

    cart_prod_6 = driver.find_element(By.XPATH, "//div[contains(text(), 'Test.allTheThings')]")
    value_cart_prod_6 = cart_prod_6.text
    print(value_cart_prod_6)
    assert value_prod_6 == value_cart_prod_6
    print("INFO CartProduct 6 Good")

    price_cart_prod_6 = driver.find_element(By.XPATH, "//div[@class='inventory_item_price']")
    value_cart_price_prod_6 = price_cart_prod_6.text
    print(value_cart_price_prod_6)
    assert value_cart_price_prod_6 == value_cart_price_prod_6
    print("INFO Cart Price Product 6 Good")

    checkout = driver.find_element(By.XPATH, "//button[@id='checkout']").click()
    print("click checkout")

    zapolnenie()

    finish_prod_6 = driver.find_element(By.XPATH, "//div[contains(text(), 'Test.allTheThings')]")
    value_finish_prod_6 = finish_prod_6.text
    print(value_finish_prod_6)
    assert value_prod_6 == value_finish_prod_6
    print("INFO finishProduct 6 Good")

    price_finish_prod_6 = driver.find_element(By.XPATH, "//div[@class='inventory_item_price']")
    value_finish_price_prod_6 = price_finish_prod_6.text
    print(value_finish_price_prod_6)
    assert value_cart_price_prod_6 == value_finish_price_prod_6
    print("INFO cart finish Product 6 Good")
    time.sleep(3)
    driver.close()
    driver.quit()


if product == '1':
    product_1()
elif product == '2':
    product_2()
elif product == '3':
    product_3()
elif product == '4':
    product_4()
elif product == '5':
    product_5()
elif product == '6':
    product_6()
else:
    print("Вы ввели недопустимый знак или символ!\nПожалуйста выберите № товрара от 1 до 6")






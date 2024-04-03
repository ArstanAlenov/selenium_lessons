import time


from selenium import webdriver
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
print("Input Login")
password = driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password_all)  #CSS.SELECTOR
print("Input Password")
button_login = driver.find_element(By.XPATH, "//input[@type = 'submit']").click()
print("Click Login Button")

"""INFO Products"""
product_1 = driver.find_element(By.XPATH, "//div[@class='inventory_item_name'][1]")
value_product_1 = product_1.text
print(value_product_1)

price_product_1 = driver.find_element(By.XPATH, "//div[@class='inventory_item_price'][1]")
value_price_product_1 = price_product_1.text
print(value_price_product_1)

product_2 = driver.find_element(By.XPATH, "//div[contains(text(), 'Bike Light')]")
value_product_2 = product_2.text
print(value_product_2)

price_product_2 = driver.find_element(By.XPATH, "(//div[@class='inventory_item_price'])[2]")
value_price_product_2 = price_product_2.text
print(value_price_product_2)


select_product_1 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']").click()
print("select_product_1")

select_product_2 = driver.find_element(By.XPATH, "//button[contains(@name, 'labs-bike')]").click()
print("select_product_2")

cart = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
print("Enter cart")


"""INFO CartProducts"""
cart_product_1 = driver.find_element(By.XPATH, "//div[@class='inventory_item_name'][1]")
value_cart_product_1 = cart_product_1.text
print(value_cart_product_1)
assert value_product_1 == value_cart_product_1
print("INFO CartProduct 1 Good")

cart_product_2 = driver.find_element(By.XPATH, "//div[contains(text(), 'Bike Light')]")
value_cart_product_2 = cart_product_2.text
print(value_cart_product_2)
assert value_product_2 == value_cart_product_2
print("INFO CartProduct 2 Good")


price_cart_product_1 = driver.find_element(By.XPATH, "//div[@class='inventory_item_price'][1]")
value_cart_price_product_1 = price_cart_product_1.text
print(value_cart_price_product_1)
assert value_cart_price_product_1 == value_cart_price_product_1
print("INFO Cart Price Product 1 Good")


price_cart_product_2 = driver.find_element(By.XPATH, "(//div[@class='inventory_item_price'])[2]")
value_cart_price_product_2 = price_cart_product_2.text
print(value_cart_price_product_2)
assert value_cart_price_product_2 == value_cart_price_product_2
print("INFO Cart Price Product 2 Good")

checkout = driver.find_element(By.XPATH, "//button[@id='checkout']").click()
print("click checkout")

"""Select User INFO"""
f_name = driver.find_element(By.XPATH, "//input[@id='first-name']")
f_name.send_keys("Olga")
print("input f_name")
l_name = driver.find_element(By.XPATH, "//input[@id='last-name']")
l_name.send_keys("Ivanova")
print("input l_name")
zip = driver.find_element(By.XPATH, "//input[@id='postal-code']")
zip.send_keys("123")
print("input zip")
contin = driver.find_element(By.XPATH, "//input[@id='continue']").click()
print("click continue")

"""INFO Finish"""
finish_product_1 = driver.find_element(By.XPATH, "//div[@class='inventory_item_name']")
value_finish_product_1 = finish_product_1.text
print(value_finish_product_1)
assert value_product_1 == value_finish_product_1
print("INFO finishProduct 1 Good")

price_finish_product_1 = driver.find_element(By.XPATH, "//div[@class='inventory_item_price']")
value_finish_price_product_1 = price_finish_product_1.text
print(value_finish_price_product_1)
assert value_cart_price_product_1 == value_finish_price_product_1
print("INFO cart finish Product 1 Good")

finish_product_2 = driver.find_element(By.XPATH, "//div[contains(text(), 'Bike Light')]")
value_finish_product_2 = finish_product_2.text
print(value_finish_product_2)
assert value_product_2 == value_finish_product_2
print("INFO finishProduct 2 Good")

price_finish_product_2 = driver.find_element(By.XPATH, "(//div[@class='inventory_item_price'])[2]")
value_finish_price_product_2 = price_finish_product_2.text
print(value_finish_price_product_2)
assert value_cart_price_product_2 == value_finish_price_product_2
print("INFO cart finish Product 2 Good")

try:
    summery_price = driver.find_element(By.XPATH, "//div[@class='summary_subtotal_label']")
    value_summery_price = summery_price.text
    print(value_summery_price.replace('$', ''))

    item_total = float(value_finish_price_product_1.replace('$', '')) + float(value_finish_price_product_2.replace('$', ''))
    print(f"Item total: {item_total}")

    assert value_summery_price == item_total
    print("Total summery price good")

finally:
    finish = driver.find_element(By.XPATH, "//button[@id='finish']").click()
    time.sleep(3)
    driver.close()





from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def check_store():

    store = {
        "buyCursor": 15,
        "buyGrandma": 100,
        "buyFactory": 500,
        "buyMine": 2000,
        "buyShipment": 7000,
        "buyAlchemy lab": 50000,
        "buyPortal": 1000000,
        "buyTime machine": 123456789

    }

    money = int(driver.find_element(By.ID, 'money').text)

    for key in store.keys():
        new_element = driver.find_element(By.ID, key)
        new_element_text = new_element.text.split('\n')
        price = new_element_text[0].split('-')[1].strip()
        price_modified = price.replace(',', '')
        new_price = int(price_modified)
        if money > new_price and new_element.get_dom_attribute('class'):
            new_element.click()


driver = webdriver.Firefox()

driver.get('https://orteil.dashnet.org/experiments/cookie/')


# TODO: click the cookie for 5 minutes

cookie = driver.find_element(By.ID, 'cookie')

timeout = time.time() + 30

while True:
    cookie.click()

    if time.time() > timeout:
        break


# TODO: Check the right pane every 5 seconds

check_store()

cursor = driver.find_element(By.ID, 'buyFactory')


# print(cursor.get_dom_attribute('class'))

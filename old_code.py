"""
Расмотрим пример улучшения на простом сценарии создание и авторизация пользователя
"""
import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = Chrome()


def authenticate(login, password):
    login_xpath = '//input[@name="username"]'
    password_xpath = '//input[@name="password"]'
    button = '//button[@name="submit"]'

    # Login
    el = driver.find_element(By.XPATH, login_xpath)
    el.clear()
    el.send_keys(login)

    # password
    el = driver.find_element(By.XPATH, password_xpath)
    el.clear()
    el.send_keys(password)

    # Еще может быть какой-нибудб костыль типа
    for _ in range(10):
        try:
            driver.find_element(By.XPATH, button).click()
            break
        except Exception:
            pass


def check_options_in_dropdown_1():
    dropdown_xpath_1 = '//select[@id="first_dropdown"]'
    options_xpath = '//select[@id="first_dropdown"]//options'
    options_list = ['public', 'private', 'include']

    dropdown_1 = driver.find_element(By.XPATH, dropdown_xpath_1)
    dropdown_1.click()

    time.sleep(1)

    els = driver.find_elements(By.XPATH, options_xpath)
    els_name = [element.text.strip() for element in els]

    assert sorted(options_list) == sorted(els_name)


def create_user(login, password):
    login_xpath = '//input[@name="username"]'
    password_xpath = '//input[@name="password"]'

    # Type account details
    dropdown_xpath_1 = '//select[@id="first_dropdown"]'
    option_1_1_xpath = '//option[contains(@text, "private")]'

    # Account role
    dropdown_xpath_2 = '//select[@id="second_dropdown"]'
    option_2_3_xpath = '//option[contains(@text, "user")]'

    button = '//button[@name="submit"]'
    # ... полей как правило бывает больше

    # Login
    el = driver.find_element(By.XPATH, login_xpath)
    el.clear()
    el.send_keys(login)

    # password
    el = driver.find_element(By.XPATH, password_xpath)
    el.clear()
    el.send_keys(password)

    dropdown_1 = driver.find_element(By.XPATH, dropdown_xpath_1)
    dropdown_1.click()

    # Wait visible option
    check_options_in_dropdown_1()
    option_1_1 = driver.find_element(By.XPATH, option_1_1_xpath)
    option_1_1.click()

    dropdown_2 = driver.find_element(By.XPATH, dropdown_xpath_2)
    dropdown_2.click()

    option_2_3 = driver.find_element(By.XPATH, option_2_3_xpath)
    option_2_3.click()

    driver.find_element(By.XPATH, button).click()

    # Ждем пока создастся пользователь
    time.sleep(10)
    #


def test_1():
    create_user('login_i', 'password')
    authenticate('login_i', 'password')
    assert not driver.current_url.endswith('authenticate')

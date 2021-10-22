import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class RegistrationPage:
    login_xpath = '//input[@name="username"]'
    password_xpath = '//input[@name="password"]'

    # Type account details
    dropdown_xpath_1 = '//select[@id="first_dropdown"]'
    option_1_1_xpath = '//option[contains(@text, "private")]'
    options_xpath = '//select[@id="first_dropdown"]//options'
    account_types = ['public', 'private', 'include']

    # Account role
    dropdown_xpath_2 = '//select[@id="second_dropdown"]'
    option_2_3_xpath = '//option[contains(@text, "user")]'

    button = '//button[@name="submit"]'

    def __init__(self, driver):
        self.driver = driver
        self.wd = WebDriverWait(self.driver, 10)

    def find_xpath(self, xpath):
        return self.wd.until(self.driver.find_element, (By.XPATH, xpath))

    def check_options_in_dropdown_1(self):
        dropdown_1 = self.find_xpath(self.dropdown_xpath_1)
        dropdown_1.click()

        els = self.find_xpath(self.options_xpath)
        els_name = [element.text.strip() for element in els]

        assert sorted(self.account_types) == sorted(els_name)

    def create_user(self, username, password):
        # Login
        el = self.find_xpath(self.login_xpath)
        el.clear()
        el.send_keys(username)

        # password
        el = self.find_xpath(self.password_xpath)
        el.clear()
        el.send_keys(password)

        dropdown_1 = self.find_xpath(self.dropdown_xpath_1)
        dropdown_1.click()

        # Wait visible option
        self.check_options_in_dropdown_1()
        option_1_1 = self.find_xpath(self.option_1_1_xpath)
        option_1_1.click()

        dropdown_2 = self.find_xpath(self.dropdown_xpath_2)
        dropdown_2.click()

        option_2_3 = self.find_xpath(self.option_2_3_xpath)
        option_2_3.click()

        self.find_xpath(self.button).click()

        # Ждем пока создастся пользователь
        time.sleep(10)

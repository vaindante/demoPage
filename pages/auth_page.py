from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class AuthPage:
    login_xpath = '//input[@name="username"]'
    password_xpath = '//input[@name="password"]'
    button = '//button[@name="submit"]'

    def __init__(self, driver):
        self.driver = driver
        self.wd = WebDriverWait(self.driver, 10)

    def find_xpath(self, xpath):
        return self.wd.until(self.driver.find_element, (By.XPATH, xpath))

    def login(self, username, password):
        # Login
        el = self.find_xpath(self.login_xpath)
        el.clear()
        el.send_keys(username)

        # password
        el = self.find_xpath(self.password_xpath)
        el.clear()
        el.send_keys(password)

        self.find_xpath(self.button).click()

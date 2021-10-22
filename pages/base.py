from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wd = WebDriverWait(self.driver, 10)

    def find_xpath(self, xpath):
        return self.wd.until(self.driver.find_element, (By.XPATH, xpath))

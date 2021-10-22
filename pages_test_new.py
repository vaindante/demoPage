from selenium.webdriver import Chrome
from pages import NewDropdownPage


def test_2():
    driver = Chrome()
    dropdown = NewDropdownPage(driver)

    dropdown.dropdown_1.check_values()
    dropdown.dropdown_1.choose()

    dropdown.dropdown_2.check_values()
    dropdown.dropdown_2.choose()

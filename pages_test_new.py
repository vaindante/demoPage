from selenium.webdriver import Chrome
from pages import OldDropdownPage


def test_2():
    driver = Chrome()
    dropdown = OldDropdownPage(driver)

    dropdown.check_options_in_dropdown_1()
    dropdown.choose_value_in_dropdown_1()

    dropdown.check_options_in_dropdown_2()
    dropdown.choose_value_in_dropdown_2()

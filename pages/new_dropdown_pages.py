from .base import BasePage
from .dropdown import Dropdown


class DropdownPage(BasePage):
    dropdown_xpath_1 = '//select[@id="first_dropdown"]'
    dropdown_first_values = ['public', 'private', 'include']

    dropdown_xpath_2 = '//select[@id="second_dropdown"]'
    dropdown_second_values = ['public', 'private', 'include']

    def __init__(self, driver):
        super().__init__(driver)
        self.dropdown_1 = Dropdown(
            self.dropdown_xpath_1,
            self.dropdown_first_values,
            'private'
        )

        self.dropdown_2 = Dropdown(
            self.dropdown_xpath_2,
            self.dropdown_second_values,
            'user'
        )

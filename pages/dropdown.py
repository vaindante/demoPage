from dataclasses import dataclass
from email.policy import default

from .base import BasePage


@dataclass
class Dropdown(BasePage):
    dropdown_xpath: str
    values: list = None
    default_choose_value: str = ''
    option_xpath: str = '//option[contains(@text, "{}")]'
    options_xpath: str = ''

    def __post_init__(self):
        self.options_xpath = self.options_xpath or f'{self.dropdown_xpath}//options'

    def check_values(self):
        dropdown = self.find_xpath(self.dropdown_xpath)
        dropdown.click()

        els = self.find_xpath(self.options_xpath)
        els_name = [element.text.strip() for element in els]

        assert sorted(self.values) == sorted(els_name)

    def choose(self, value=None):
        value = value or self.default_choose_value
        self.find_xpath(self.option_xpath.format(value)).click()

from .base import BasePage


class DropdownPage(BasePage):
    # Type account details
    dropdown_xpath_1 = '//select[@id="first_dropdown"]'
    option_1_1_xpath = '//option[contains(@text, "private")]'
    dropdown_1_options_xpath = '//select[@id="first_dropdown"]//options'
    dropdown_first_values = ['public', 'private', 'include']

    # Account role
    dropdown_xpath_2 = '//select[@id="second_dropdown"]'
    option_2_3_xpath = '//option[contains(@text, "user")]'
    dropdown_2_options_xpath = '//select[@id="second_dropdown"]//options'
    dropdown_second_values = ['public', 'private', 'include']

    def check_options_in_dropdown_1(self):
        dropdown = self.find_xpath(self.dropdown_xpath_1)
        dropdown.click()

        els = self.find_xpath(self.dropdown_1_options_xpath)
        els_name = [element.text.strip() for element in els]

        assert sorted(self.dropdown_first_values) == sorted(els_name)

    def choose_value_in_dropdown_1(self):
        option = self.find_xpath(self.option_1_1_xpath)
        option.click()

    def check_options_in_dropdown_2(self):
        dropdown = self.find_xpath(self.dropdown_xpath_1)
        dropdown.click()

        els = self.find_xpath(self.dropdown_1_options_xpath)
        els_name = [element.text.strip() for element in els]

        assert sorted(self.dropdown_first_values) == sorted(els_name)

    def choose_value_in_dropdown_2(self):
        option = self.find_xpath(self.option_2_3_xpath)
        option.click()

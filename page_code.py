from selenium.webdriver import Chrome
from pages import AuthPage, RegistrationPage


def test_1():
    driver = Chrome()
    auth_page = AuthPage(driver)
    registration_page = RegistrationPage(driver)

    registration_page.create_user('login_1', 'password')
    auth_page.login('login_1', 'password')

    assert auth_page.driver.current_url.endswith('authenticate')

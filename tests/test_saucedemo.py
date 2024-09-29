from time import sleep

from selenium import webdriver
from pages.login_page import LoginPage
from pages.logout_page import LogoutPage
import  pytest
from  resources import  config

@pytest.fixture(scope="module")
def setup_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver  # This will return the driver to the test function
    driver.quit()  # This will run after all tests in the module

def test_login_valid(setup_driver):
    driver = setup_driver
    driver.get(config.url)
    login_page = LoginPage(driver)
    logout_page=LogoutPage(driver)
    login_page.enter_username(config.username)
    login_page.enter_password(config.password)
    login_page.click_login()
    sleep(2)
    title = login_page.get_title()
    assert "Swag Labs" in title
    logout_page.logout()
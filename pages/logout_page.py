from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

class LogoutPage:
    def __init__(self, driver):
        self.driver = driver

    def click_burger_menu(self):
        burger_menu = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "react-burger-menu-btn"))
        )
        burger_menu.click()


    def click_logout(self):
        logout_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
        )
        logout_button.click()


    def logout(self):
        self.click_burger_menu()
        self.click_logout()

    def click_reset(self):
        reset_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "reset_sidebar_link"))
        )
        reset_button.click()


    def click_cross_button(self):
        cross_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "react-burger-cross-btn"))
        )
        cross_button.click()


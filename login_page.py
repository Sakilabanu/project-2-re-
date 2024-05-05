from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from locators.all_locators import Locators




class Do_Login:

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def do_login(self, username, password):

        user_na = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.NAME, Locators.l_username_name))
        user_na.clear()
        user_na.s(username)
        pwd = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.NAME, Locators.l_password_name))
        pwd.clear()
        pwd.send_keys(password)
        l_btn = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(BY.NAME, Locators.login_btn_name))
        l_btn.click()
        try:
            alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
            alert.accept()  # Accept the alert
        except:
            pass
        driver.implicitly_wait(20)
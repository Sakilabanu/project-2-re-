from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from locators.all_locators import Locators

class Reset_pass:

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def reset_password(self, username):

        forget_pass_btn = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(By.LINK_TEXT, Locators.forgot_pass_link_text))
        forget_pass_btn.click()

        driver.implicitly_wait(20)

        user_name = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(By.NAME, Locators.reset_user_name))
        user_name.send_keys(username)

        submitting_reset = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.LINK_TEXT, Locators.reset_pwd_btn_link_text))
        submitting_reset.click()

        driver.implicitly_wait(20)
        return self.do_login()
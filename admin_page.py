from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from locators.all_locators import Locators


class Admin_page:

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def click_admin_module(self):
        admin = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(By.XPATH, Locators.admin_module_xpath))
        admin.click()

    def is_visible(self, value):
        element = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(value))
        return bool(element)

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    def validate_headers(self):

        valid_header = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_all_elements_located(By.XPATH, "//div[contains(@class, 'oxd-topbar-body')]"))
        print(len(valid_header))

        # Find all <span> elements
        span_elements = WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located(By.TAG_NAME, 'span'))

        # Define the class name you're looking for
        desired_class = "oxd-topbar-body-nav-tab-item"

        # Iterate over each <span> element
        for span in span_elements:
            # Check if the span has the desired class
            if desired_class in span.get_attribute("class"):
                # Get the text inside the span
                span_text = span.text
                print(span_text)

    # ----------------------------- getting text of all headers -01
    #
    # for list in valid_header:
    #     print(list.get_dom_attribute(valid_header).text)

    # ------------------------------ getting text of all headers -02
    # check_header_list = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(By.XPATH, "//nav[@role= 'navigation' and contains(@class, 'oxd-topbar-body-nav'])"))
    # print(len(check_header_list))
    #
    # get_headers_texts = WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located(By.XPATH, "//*[@id ='app' and contains(@class, 'oxd-topbar-body-nav-tab')]"))
    # print(get_headers_texts)
    #
    # for text in get_headers_texts:
    #     all_texts = text.get_attribute('class')
    #     all_texts.__getitem__(get_headers_texts)
    #     if all_texts == 'oxd-topbar-body-nav-tab':
    #         print((all_texts).text)
    # ------------------------------

    def validate_side_menu(self):

        valid_side_menu = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_all_elements_located(By.XPATH, "//div[contains(@class, 'oxd-topbar-body')]"))
        print(len(valid_side_menu))

        # Find all <span> elements
        span_elements = WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located(By.TAG_NAME, 'span'))

        # Define the class name you're looking for
        desired_class = "oxd-text oxd-text--span oxd-main-menu-item--name"

        # Iterate over each <span> element
        for span in span_elements:
            # Check if the span has the desired class
            if desired_class in span.get_attribute("class"):
                # Get the text inside the span
                span_text = span.text
                print(span_text)
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

driver = None
driver_path = (r"C:\Users\sahbi\OneDrive\Desktop\PyCharm Community Edition 2023.2.5\chromedriver.exe")
OHRM_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

@pytest.fixture(scope="class")
def chrome_driver(request):

    # Setup Chrome driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(OHRM_url)
    request.cls.driver = OHRM_url

    yield driver
    # Teardown Chrome driver
    driver.quit()
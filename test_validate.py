from config_pack.config import Get_url
from locators.all_locators import Locators
from pages_pack.Reset_password_page import Reset_pass
from pages_pack.login_page import Do_Login
from pages_pack.admin_page import Admin_page



@pytest.mark.usefixtures("chrome_driver")
class Test_validate:

    #TC_PIM_01
    def test_reset_password(self):

        try:
            reset = Reset_pass(self.driver)
            reset.reset_password(Get_url.username)

            exp_url = reset.is_visible(Get_url.reset_password_success_url)
            assert self.current_url == exp_url, "go and check the TC_PIM_01"
            print("Reset Password link sent successfully")

        except Exception as e:
            print("something went wrong in test_reset_password is ", e)


    #TC_PIM_02
    def test_validate_header(self):

        try:
            # entering the login.
            login = Do_Login(self.driver)
            login.do_login(Get_url.username, Get_url.password)

            # click the admin module.
            admin = Admin_page(self.driver)
            display_headers = admin.click_admin_module()

            # validate the title.
            exp_title = admin.get_title(Get_url.Admin_page_Title)
            assert self.current_title == exp_title, "go and check validate the title in TC_PIM_02"
            print("got the title of OrangeHRM is performed successfully")

            # validate the header texts.
            admin.validate_headers()

            display_headers.is_displayed()
            assert self.current_url == Get_url.admin_page_url, "go and check the TC_PIM_02"
            print("Admin Page Header successfully displayed")

        except Exception as e:
            print("something went wrong in test_validate_header", e)


    # TC_PIM_03
    def test_validate_side_menu(self):

        try:
            # entering the login.
            login = Do_Login(self.driver)
            login.do_login(Get_url.username, Get_url.password)

            # click the admin module.
            admin = Admin_page(self.driver)
            display_side_menu = admin.click_admin_module()

            # validate the side-menu texts.
            admin.validate_side_menu()

            display_side_menu.is_displayed()
            assert self.current_url == Get_url.admin_page_url, "go and check the TC_PIM_03"
            print("Admin Page side-menu successfully displayed")

        except Exception as e:
            print("something went wrong in test_validate_side_menu", e)
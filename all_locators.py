class Locators:

    def __init__(self, driver):
        self.driver = driver


##### Login page locators ######

    l_username_name = 'username'
    l_password_name = 'password'
    login_btn_name = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
    forgot_pass_link_text = 'Forgot your password? '

##### reset password locators #####

    reset_user_name = 'username'
    reset_pwd_btn_link_text = ' Reset Password '
    admin_module_xpath = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]'
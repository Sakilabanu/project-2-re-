class Get_url:

    def __init__(self, driver):
        self.driver = driver

#### url of after sending reset password link ####

    reset_password_success_url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/sendPasswordReset'

#### admin page's title,url ####

    Admin_page_Title = 'OrangeHRM'
    admin_page_url = 'https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers'

#### datas for login ####

    username = "Admin"
    password = "admin123"
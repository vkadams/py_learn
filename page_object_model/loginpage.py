from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        # self. as we want to make these as class variables whcih can be access by creating object of class
        self.page = page
        self.login_link = self.page.locator('#login2')
        self.user_input = self.page.locator('#loginusername')
        self.password_input = self.page.locator('#loginpassword')
        self.login_button = self.page.locator('button:has-text("Log in")')

    # action methods

    def click_login_link(self):
        self.login_link.click()

    def enter_username(self, username):
        self.user_input.fill("")
        self.user_input.fill(username)

    def enter_password(self, password):
        self.password_input.fill("")
        self.password_input.fill(password)

    def click_login_button(self):
        self.login_button.click()

    # additional login method-- combines complete login action
    def perform_login(self, username, password):
        self.login_link.click()
        self.user_input.fill("")
        self.user_input.fill(username)
        self.password_input.fill("")
        self.password_input.fill(password)
        self.login_button.click()


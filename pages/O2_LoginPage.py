from playwright.sync_api import Page, expect

from utils.config_reader import config
class LoginPage:

    def __init__(self, page: Page):
        self.page = page
        self.login_by_github_button = page.get_by_role("button", name="Continue with GitHub")
        self.email_input = page.get_by_placeholder("Email")
        self.password_input = page.get_by_placeholder("Password")
        self.sign_in_button = page.get_by_role("button", name="Login", exact=True)
        self.login_page_title = page.get_by_text("Sign in to GitHub")
        self.user_logo = page.locator("button[data-test='header-my-account-profile-icon']")

    def open_application(self):
        self.page.goto(config["TESTDATA"]["local_host"])

    def login_into_app(self):
        user_email = config['TESTDATA']['username']
        user_password = config['TESTDATA']['password']
        self.email_input.fill(user_email)
        self.password_input.fill(user_password)
        self.sign_in_button.click()
        self.page.wait_for_timeout(3000)
        expect(self.user_logo).to_be_visible(timeout=3000)
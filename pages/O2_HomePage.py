from playwright.sync_api import Page, expect

from utils.config_reader import config
class HomePage:

    def __init__(self, page: Page):
        self.page = page
        self.menu_dashboard = page.locator('a[data-test="menu-link-/dashboards-item"]')
        self.menu_dashboard2 = page.locator('a[data-test="menu-link-/dashboards-item"]')
        self.add_dashboard_button = page.locator('[data-test="dashboard-add"]')

    def navigate_to_dashboard(self):
        self.menu_dashboard.click()
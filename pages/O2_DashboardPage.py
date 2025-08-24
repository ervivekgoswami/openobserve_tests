from playwright.sync_api import Page, expect

from utils.config_reader import config
class DashboardPage:

    def __init__(self, page: Page):
        self.page = page
        self.add_new_dashboard_button = page.get_by_role("button",name="New Dashboard")
        self.new_dashboard_name = page.locator('[data-test="add-dashboard-name"]')
        self.new_dashboard_desc = page.locator('[data-test="add-dashboard-description"]')
        self.new_dashboard_folder = page.locator('[data-test="index-dropdown-stream_type"]')
        self.save_new_dashboard_button = page.locator('button[data-test="dashboard-add-submit"]')
        self.new_dashboard_success_msg = page.locator('div[class="q-notification__message col"]')
        self.panel_name = page.locator('div[class="panelHeader"]')
        self.open_dashboard = page.get_by_role("cell", name="Auto Dashboard")
        self.panel_options = page.locator('[data-test="dashboard-edit-panel-Line Chart Panel-dropdown"]')
        self.panel_edit_option = page.locator('[data-test="dashboard-edit-panel"]')



    def create_new_dashboard(self,dashboard_name,dashboard_desc):
        expect(self.add_new_dashboard_button).to_be_visible(timeout=10000)
        self.add_new_dashboard_button.click()
        expect(self.new_dashboard_name).to_be_visible(timeout=10000)
        self.new_dashboard_name.fill(dashboard_name)
        self.new_dashboard_desc.fill(dashboard_desc)
        self.new_dashboard_folder.click()
        self.page.get_by_role("option", name="default").click()
        self.save_new_dashboard_button.click()
        self.page.wait_for_timeout(timeout=3000)
        expect(self.new_dashboard_success_msg).to_have_text("Dashboard added successfully.")

    def verify_panel_added(self,panel_name_text):
        expect(self.panel_name).to_have_text(panel_name_text)

    def edit_dashboard(self,dashboard_name):
        self.page.get_by_role("cell", name=dashboard_name).click()
        expect(self.panel_name).to_be_visible(timeout=10000)
        self.panel_options.click()
        expect(self.panel_edit_option).to_be_visible(timeout=10000)
        self.panel_edit_option.click()
        self.page.wait_for_timeout(3000)
        expect(self.page.locator("#app")).to_contain_text("Edit Panel")



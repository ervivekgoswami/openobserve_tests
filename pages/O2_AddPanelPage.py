from playwright.sync_api import Page, expect

from utils.config_reader import config

class AddPanelPage:

    def __init__(self, page: Page):
        self.page = page
        self.add_panel_button = page.locator('[data-test="dashboard-if-no-panel-add-panel-btn"]')
        self.panel_name_input = page.locator('[data-test="dashboard-panel-name"]')
        self.panel_Y_axis = page.locator('[data-test="field-list-item-logs-windows-body_channel"] [data-test="dashboard-add-y-data"]')
        self.panel_breakdown = page.locator('[data-test="field-list-item-logs-windows-body_channel"] [data-test="dashboard-add-b-data"]')
        self.apply_button = page.locator('[data-test="dashboard-apply"]')
        self.select_line_chart = page.locator('[data-test="selected-chart-line-item"] img')
        self.save_panel = page.locator('[data-test="dashboard-panel-save"]')
        self.line_chart = page.locator('div[role="img"]')
        self.open_configs = page.locator('[data-test="dashboard-sidebar"]')
        self.connect_null_values = page.locator('[data-test="dashboard-config-connect-null-values"] div').nth(2)
        self.update_chart_msg = page.get_by_text("Your chart is not up to date")
        self.add_other_series = page.locator("[data-test=\"dashboard-config-top_results_others\"] div").nth(2)


    def add_panel_to_dashboard(self,panel_name):
        expect(self.add_panel_button).to_be_visible(timeout=10000)
        self.add_panel_button.click()
        self.select_line_chart.click()
        expect(self.panel_name_input).to_be_visible(timeout=10000)
        self.panel_name_input.fill(panel_name)
        self.panel_Y_axis.click()
        self.panel_breakdown.click()
        expect(self.apply_button).to_be_enabled(timeout=10000)
        self.apply_button.click()
        expect(self.page.locator("canvas").nth(2)).to_be_visible()
        self.save_panel.click()

    def add_connect_null_value_config_to_panel(self):
        self.open_configs.click()
        self.connect_null_values.click()
        expect(self.update_chart_msg).to_be_visible()
        expect(self.apply_button).to_be_enabled(timeout=10000)
        self.apply_button.click()
        expect(self.page.locator("canvas").nth(2)).to_be_visible()
        self.save_panel.click()

    def add_other_series_config_to_panel(self):
        self.open_configs.click()
        self.add_other_series.click()
        expect(self.update_chart_msg).to_be_visible()
        expect(self.apply_button).to_be_enabled(timeout=10000)
        self.apply_button.click()
        expect(self.page.locator("canvas").nth(2)).to_be_visible()
        self.save_panel.click()



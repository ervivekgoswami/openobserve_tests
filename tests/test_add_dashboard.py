from utils.config_reader import config

dashboard_name = 'Auto Dashboard'
dashboard_desc = 'This is for Line Chart'
panel_name = 'Line Chart Panel'
def test_add_new_line_dashboard(home_page,dashboard_page,addpanel_page):
    home_page.navigate_to_dashboard()
    dashboard_page.create_new_dashboard(dashboard_name,dashboard_desc)
    addpanel_page.add_panel_to_dashboard(panel_name)
    dashboard_page.verify_panel_added(panel_name)

def test_connect_null_values(home_page,dashboard_page,addpanel_page):
    home_page.navigate_to_dashboard()
    dashboard_page.edit_dashboard(dashboard_name)
    addpanel_page.add_connect_null_value_config_to_panel()
    dashboard_page.verify_panel_added(panel_name)

def test_add_other_series(home_page,dashboard_page,addpanel_page):
    home_page.navigate_to_dashboard()
    dashboard_page.edit_dashboard(dashboard_name)
    addpanel_page.add_other_series_config_to_panel()
    dashboard_page.verify_panel_added(panel_name)
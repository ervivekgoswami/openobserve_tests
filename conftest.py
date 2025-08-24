import pytest
from playwright.sync_api import Page,Playwright, sync_playwright, expect
from pages.O2_AddPanelPage import AddPanelPage
from pages.O2_DashboardPage import DashboardPage
from pages.O2_HomePage import HomePage
from pages.O2_LoginPage import LoginPage
from utils.config_reader import config


@pytest.fixture(scope="function",autouse=True)
def before_each_test(login_page):
    login_page.open_application()
    login_page.login_into_app()


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    # Optionally, you can log in here if needed
    login_page = LoginPage(page)
    return login_page

@pytest.fixture
def home_page(page: Page) -> HomePage:
    # Optionally, you can log in here if needed
    home_page = HomePage(page)
    return home_page

@pytest.fixture
def dashboard_page(page: Page) -> DashboardPage:
    # Optionally, you can log in here if needed
    dashboard_page = DashboardPage(page)
    return dashboard_page

@pytest.fixture
def addpanel_page(page: Page) -> AddPanelPage:
    # Optionally, you can log in here if needed
    addpanel_page = AddPanelPage(page)
    return addpanel_page

@pytest.fixture(scope="session")
def api_request_context(playwright: Playwright):
    # Create API request context
    request_context = playwright.request.new_context(
        base_url=config["TESTDATA"]["local_host"]
    )
    yield request_context
    request_context.dispose()

import pytest
from config.driver_setup import get_driver
from pages.login_page import LoginPage
from utils.common import take_screenshot


@pytest.fixture(scope="class")
def driver():
    driver = get_driver()
    yield driver
    driver.quit()


@pytest.mark.usefixtures("driver")
class TestLogin:
    def test_login_success(self, driver):
        login_page = LoginPage(driver)
        login_page.enter_username("test_user")
        login_page.enter_password("password123")
        login_page.click_login()
        take_screenshot(driver, "test_login_success")

    def test_login_invalid_credentials(self, driver):
        login_page = LoginPage(driver)
        login_page.enter_username("invalid_user")
        login_page.enter_password("wrong_password")
        login_page.click_login()
        take_screenshot(driver, "test_login_invalid_credentials")

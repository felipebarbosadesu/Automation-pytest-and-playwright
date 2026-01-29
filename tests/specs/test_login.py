import pytest
from tests.pages.login_page import LoginPage

@pytest.mark.parametrize("username", [
    "standard_user",
    "problem_user",
    "performance_glitch_user",
    "error_user",
    "visual_user",
])
@pytest.mark.smoke
def test_login_valid_users(page, username):
    LoginPage(page).login(username, "secret_sauce")
    page.wait_for_url("**/inventory.html")

@pytest.mark.smoke
def test_login_locked_out_user_shows_error(page):
    LoginPage(page).login("locked_out_user", "secret_sauce")
    assert page.is_visible('[data-test="error"]')

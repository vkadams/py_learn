import pytest
from playwright.sync_api import Page, expect

'''
scenarios-
data valid-- login success-- passed
data valid-- login fail-- failed
data invalid-- login success-- failed
data invalid-- login fail-- passed
'''
login_test_data=[("laura.taylor1234@example.com", "test123", "valid"),
("invaliduser@example.com", "test321", "invalid"),
("validuser@example.com", "testxyz", "invalid"),
("", "", "invalid")]

@pytest.mark.parametrize("email, password, validity",login_test_data)
def test_login_datadriven(email, password, validity, page: Page):
    # login form
    page.goto("https://demowebshop.tricentis.com/login")
    page.locator('#Email').fill(email)
    page.locator('#Password').fill(password)
    page.locator('input[value="Log in"]').click()

    # validation
    if validity == "valid":
        expect(page.locator('.ico-logout')).to_be_visible(timeout=5000) #logout link
    else:
        expect(page.locator(".validation-summary-errors")).to_be_visible(timeout=5000)
        expect(page).to_have_url("https://demowebshop.tricentis.com/login")


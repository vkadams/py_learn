import pytest
from playwright.sync_api import Page, Playwright, expect


# https://the-internet.herokuapp.com/basic_auth
# https://admin:admin@the-internet.herokuapp.com/basic_auth

@pytest.mark.skip()
def test_auth_popup(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    # credentails are passed in the URL
    page.goto("https://admin:admin@the-internet.herokuapp.com/basic_auth")
    #page.wait_for_timeout(3000)
    page.wait_for_load_state()
    expect(page.locator('div[class="example"] p')).to_be_visible()
    page.wait_for_timeout(3000)


def test_auth_popup_context(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    # credentials will be passed in the context-- this is preferred
    # testing the credential will be in separate properties file
    context = browser.new_context(http_credentials={'username': 'admin', 'password': 'admin'})
    page = context.new_page()
    # credentails are passed in the URL
    page.goto("https://the-internet.herokuapp.com/basic_auth")
    #page.wait_for_timeout(3000)
    page.wait_for_load_state()
    expect(page.locator('div[class="example"] p')).to_be_visible()
    page.wait_for_timeout(3000)

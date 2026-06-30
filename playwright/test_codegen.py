import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://demoblaze.com/index.html")
    expect(page.get_by_role("link", name="PRODUCT STORE")).to_be_visible()
    page.get_by_role("link", name="Log in").click()
    page.locator("#loginusername").fill("pavanol")
    page.locator("#loginpassword").fill("test@123")
    page.get_by_role("button", name="Log in").click()
    page.wait_for_timeout(3000)
    expect(page.get_by_role("link", name="Log out")).to_be_visible()
    expect(page.locator("#nameofuser")).to_contain_text("Welcome pavanol")
    page.get_by_role("link", name="Log out").click()
    expect(page.get_by_role("link", name="Log in")).to_be_visible()

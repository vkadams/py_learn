import pytest
from playwright.sync_api import Page, expect

@pytest.mark.skip()
def test_confirmation_dialog_ok(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.on("dialog", lambda dialog:dialog.accept())
    page.locator('#confirmBtn').click()
    text = page.locator('#demo').inner_text()
    print(text)
    expect(page.locator('#demo')).to_have_text("You pressed OK!")
    page.wait_for_timeout(3000)


def test_confirmation_dialog_cancel(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.on("dialog", lambda dialog:dialog.dismiss())
    page.locator('#confirmBtn').click()
    text = page.locator('#demo').inner_text()
    print(text)
    expect(page.locator('#demo')).to_have_text("You pressed Cancel!")
    page.wait_for_timeout(3000)
import pytest
from playwright.sync_api import Page, expect

@pytest.mark.skip()
def test_prompt_dialog_ok(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.on('dialog', lambda dialog:dialog.accept('Tommy Boy'))
    page.locator('#promptBtn').click()
    text = page.locator('#demo').inner_text()
    print(text)
    expect(page.locator('#demo')).to_contain_text('Tommy Boy')
    page.wait_for_timeout(3000)


def test_prompt_dialog_cancel(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.on('dialog', lambda dialog:dialog.dismiss())
    page.locator('#promptBtn').click()
    text = page.locator('#demo').inner_text()
    print(text)
    expect(page.locator('#demo')).to_have_text("User cancelled the prompt.")
    page.wait_for_timeout(3000)
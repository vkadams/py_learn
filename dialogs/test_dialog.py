from playwright.sync_api import Page, expect
import pytest

@pytest.mark.skip()
def test_sample_dialog(page:Page):
    page.goto('https://testautomationpractice.blogspot.com/')
    page.wait_for_timeout(3000)
    # approach 1- not much preferred
    # create user defined function
    def handle_dialog(dialog):
        dialog.accept()
    # before clicking on alert button we need to register the event
    page.on("dialog",handle_dialog)
    page.locator('#alertBtn').click()
    page.wait_for_timeout(3000)

def test_sample_dialog_another_approach(page:Page):
    page.goto('https://testautomationpractice.blogspot.com/')
    page.on("dialog", lambda dialog:dialog.accept())
    page.locator('#alertBtn').click()
    page.wait_for_timeout(3000)

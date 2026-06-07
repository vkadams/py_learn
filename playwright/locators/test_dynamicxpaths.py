import pytest
from playwright.sync_api import Page, expect
import re

def test_dynamic_xpath(page: Page):
    page.goto('https://testautomationpractice.blogspot.com/p/playwrightpractice.html')

    # using or operator
    start_stop_button = page.locator('//button[text()="START" or text()="STOP"]')
    # using starts-with page.locator('//button[starts-with(text(),"ST")]')
    # using contains page.locator('//button[contains(text(),"ST")]')

    # clicking on the button 5 times
    # for i in range(5):
    #     start_stop_button.click()
    #     page.wait_for_timeout(2000)



def test_dynamic_css(page: Page):
    page.goto('https://testautomationpractice.blogspot.com/p/playwrightpractice.html')
    btn = page.locator('button[name="start"],button[name="stop"]')
    # using starts with-  page.locator('button[name^="st"]')
    # using contains-  page.locator('button[name*="st"]')
    for i in range(5):
        btn.click()
        page.wait_for_timeout(2000)


def test_dynamic_playwright_locators(page: Page):
    page.goto('https://testautomationpractice.blogspot.com/p/playwrightpractice.html')
    buttn = page.get_by_role('button',name=re.compile(r'ST.*'))
    for i in range(5):
        buttn.click()
        page.wait_for_timeout(2000)
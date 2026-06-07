import pytest
from playwright.sync_api import Page, Playwright, expect

def test_tabs(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    parentpage = context.new_page()
    parentpage.goto("https://testautomationpractice.blogspot.com/")

    # clicking button to open new tab is an event
    parentpage.on("page", lambda page: page.wait_for_load_state())
    parentpage.locator('button:has-text("New Tab")').click()
    parentpage.wait_for_timeout(3000)

    all_tabs = context.pages
    print('Number of tabs-',len(all_tabs))
    print('Title of parent page', all_tabs[0].title())
    print('Title of child page/tab', all_tabs[1].title())

    childpage = all_tabs[1]
    print('URL of child page', childpage.url)
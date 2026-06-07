from playwright.sync_api import Page, Playwright, expect

'''
Browser-- > one context --> multiple pages
we are not passing page fixture- we will use playwright fixture
'''

def test_browser_context(playwright:Playwright):
    # created our own browser
    browser = playwright.chromium.launch(headless=False)
    # created our own context, we can create multiple contexts
    context = browser.new_context()
    # create a new page- we can create multiple pages
    page1 = context.new_page()
    page2 = context.new_page()
    # benefit of creating multiple pages is that
    # we can interact with multiple urls at same time

    page1.goto("https://playwright.dev/docs/intro")
    expect(page1).to_have_title("Installation | Playwright")
    page1.wait_for_timeout(3000)

    page2.goto("https://www.selenium.dev/")
    expect(page2).to_have_title("Selenium")
    page2.wait_for_timeout(3000)


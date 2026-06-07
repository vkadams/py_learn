from playwright.sync_api import Playwright, expect

def test_tracing(playwright: Playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    # we need to start trace as soon as context is ready
    context.tracing.start(screenshots=True, snapshots=True)
    page = context.new_page()

    page.goto("https://demoblaze.com/")
    page.locator('#login2').click()
    page.locator('#loginusername').fill("pavanol")
    page.locator('#loginpassword').fill("test@123")
    page.locator('button[onclick="logIn()"]').click()

    page.wait_for_timeout(3000)

    expect(page.locator('#logout2')).to_be_visible()
    expect(page.locator('#nameofuser')).to_contain_text('Welcome pavanol')
    #page.wait_for_timeout(3000)

    context.tracing.stop(path="trace.zip")

    page.close()
    # print(page.video)
    context.close()
    # print(page.video.path())
    browser.close()

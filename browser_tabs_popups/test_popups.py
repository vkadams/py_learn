from playwright.sync_api import Page, Playwright, expect

def test_handle_popups(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    #page = browser.new_context(viewport={"width": 1900, "height": 1000}).new_page()
    page.goto("https://testautomationpractice.blogspot.com/")
    # the test is open popups from page which is a event requires handling-
    page.on("popup", lambda popup: popup.wait_for_load_state())
    page.locator('#PopUp').click()
    page.wait_for_timeout(3000)

    # getting number of pages
    all_popups = context.pages
    print("all popups loaded-", len(all_popups))

    # capture urls of all poppup pages and perform some action/s
    #title = list()
    for popup in all_popups:
        print('URL of the popup',popup.url)
        #title.append(popup.title)
        title = popup.title()
        if "Playwright" in title:
            popup.locator(".getStarted_Sjon").click() # notice we use popup & not page
            popup.wait_for_timeout(3000)
            # Installation | Playwright Python
            expect(popup).to_have_title("Installation | Playwright")
            popup.close()
        if "Selenium" in title:
            popup.locator('a[href="/about/"]').click()
            popup.wait_for_timeout(3000)
            expect(popup).to_have_title("About Selenium | Selenium")
            popup.close()

    page.wait_for_timeout(3000)
    context.close()
    browser.close()



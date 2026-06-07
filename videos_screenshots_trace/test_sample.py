from playwright.sync_api import Page, expect

# need to generate videos/screenshots/trace
'''
create pytest.ini file in the project root == this is pytest specific & not playwright feature
need to run the test only thru command prompt/terminal
pytest will create test-results folder where results are stored- trace.zip/video/screenshots
'''

def test_url(page: Page):
    page.goto("https://demoblaze.com/")
    expect(page).to_have_url("https://demoblaze.com/")

def test_title(page: Page):
    page.goto("https://demoblaze.com/")
    expect(page).to_have_title("STORE")

def test_login(page: Page):
    page.goto("https://demoblaze.com/")
    page.locator('#login2').click()
    page.locator('#loginusername').fill("pavanol")
    page.locator('#loginpassword').fill("test@123")
    page.locator('button[onclick="logIn()"]').click()
    page.wait_for_timeout(3000)
    expect(page.locator('#logout2')).to_be_visible()
    expect(page.locator('#nameofuser')).to_contain_text('Welcome pavanol')
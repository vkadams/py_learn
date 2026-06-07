# importing page fixture is step 1
from playwright.sync_api import Page, expect

# launch web page & verify URL
def test_verifypageurl(page:Page):
    page.goto('https://automationexercise.com/') # by default it will launch Chrome browser
    myurl = page.url
    print('URL of the application:',myurl)
    # we can use playwright assertion-'expect' instead of pytest assertions
    expect(page).to_have_url('https://automationexercise.com/')

def test_verifypagetitle(page:Page):
    page.goto('https://automationexercise.com/')
    pagetitle = page.title()
    print('Title of the app:',pagetitle)
    expect(page).to_have_title('Automation Exercise')
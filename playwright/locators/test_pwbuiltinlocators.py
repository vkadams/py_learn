from playwright.sync_api import Page, expect
import re

def test_verify_pwlocators(page: Page):
    page.goto('https://demowebshop.tricentis.com/')

    # 1 get_by_alt_text -- typically images have this
    # time.sleep(5) -- this is from python
    # from playwright
    page.wait_for_timeout(3000)
    logo = page.get_by_alt_text('Tricentis Demo Web Shop')
    expect(logo).to_be_visible()

    # 2 get_by_text
    expect(page.get_by_text('Featured products')).to_be_visible()
    # using regular expression
    expect(page.get_by_text(re.compile('.*Featured.*'))).to_be_visible()

    # 3 get_by_role
    page.goto('https://demowebshop.tricentis.com/register')
    page.wait_for_timeout(3000)
    expect(page.get_by_role('heading',name='Register')).to_be_visible()

    # 4 get_by_label
    page.get_by_label('First name:').fill('John')
    page.get_by_label('Last name:').fill('Doe')
    page.get_by_label('Email:').fill('john.doe@example.com')
    page.wait_for_timeout(3000)

    # 5 get_by_placeholder
    page.goto('https://automationbookstore.dev/')
    page.get_by_placeholder('Filter books..').fill('automation')
    page.wait_for_timeout(3000)

    # 6 get_by_title
    page.goto('https://testautomationpractice.blogspot.com/p/playwrightpractice.html')
    expect(page.get_by_title('Home page link')).to_have_text('Home')
    expect(page.get_by_title('HyperText Markup Language')).to_have_text('HTML')
    page.wait_for_timeout(3000)

    # 7 get_by_test_id
    expect(page.get_by_test_id('profile-name')).to_have_text('John Doe')
    expect(page.get_by_test_id('profile-email')).to_have_text('john.doe@example.com')
    page.wait_for_timeout(3000)

    # orange hrm login & check dashboard displayed
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    page.get_by_placeholder('Username').fill('Admin')
    page.get_by_placeholder('Password').fill('admin123')
    page.get_by_role('button',name='Login').click()
    expect(page.get_by_role('heading', name='Dashboard')).to_be_visible()
    page.wait_for_timeout(3000)
    page.close()




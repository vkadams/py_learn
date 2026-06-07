'''
tag id      -  tag#id
tag class   - tag.class
tag attribute - tag[attribute=value]
tag class attribute - tag.class[attribute=value]
'''

from playwright.sync_api import Page, expect

def test_verify_css_locators(page: Page):
    # page.goto('https://demowebshop.tricentis.com/')
    # # tag id
    # page.locator('input#small-searchterms').fill('T-Shirts')

    # tag class
    # page.goto('https://testautomationpractice.blogspot.com/p/playwrightpractice.html')
    # page.locator('input.wikipedia-search-input').fill('Hello')

    # tag attribute
    page.goto('https://demowebshop.tricentis.com/')
    #page.locator('input[value="Search store"]').fill('T-Shirts')

    # tag class attribute
    page.locator('input.wikipedia-search-input[name="q"]').fill('T-Shirts')
    page.wait_for_timeout(3000)

# usage of not attribute
'''
match the paragraph that has this class & not the id:
p:not([#id])[class='hello'] 
match the paragraph that has neither this id nor the class:
p:not([#id]):not([class='hello'])

getting immediate sibling below
p[id='hello']+p
'''

def test_css_check(page: Page):
    page.goto('https://demowebshop.tricentis.com/')
    # logo visibility
    expect(page.locator('img[alt="Tricentis Demo Web Shop"]')).to_be_visible()

    # find computers
    computers = page.locator('.product-grid a[title*="omputer"]')
    expect(computers).to_have_count(4)

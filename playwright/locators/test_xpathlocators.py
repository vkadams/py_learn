import pytest
from playwright.sync_api import Page, expect

def test_xpath_locators(page: Page):
    page.goto('https://demowebshop.tricentis.com/')
    expect(page.locator('//img[@alt="Tricentis Demo Web Shop"]')).to_be_visible()

    # xpath with contains()
    products = page.locator('//h2//a[contains(@href,"omputer")]')
    print(products.count())
    expect(products).to_have_count(products.count())

    # get product title of above products
    # text_content()-- will only return textcontent of one element
    print(products.first.text_content()) # nth(0)
    print(products.nth(1).text_content())
    print(products.nth(2).text_content())
    print(products.last.text_content())

    # text contents of all products
    # all_text_contents() returns list()
    print(type(products.all_text_contents())) # returns list
    for product in products.all_text_contents():
        print('Product name is:',product)

    # starts-with()
    products_startng_build =page.locator('//h2//a[starts-with(text(),"Build")]')
    print(products_startng_build.all_text_contents()) # ['Build your own cheap computer', 'Build your own computer', 'Build your own expensive computer']

    # text() -- inner text of the element
    expect(page.locator('//a[text()="Register"]')).to_be_visible()

    # last() -- google+ from footer
    google_plus = page.locator('//div[@class="column follow-us"]//li[last()]')
    expect(google_plus).to_have_text('Google+')

    # with position()
    twitter_link = page.locator('//div[@class="column follow-us"]//li[position()=2]')
    expect(twitter_link).to_have_text('Twitter')



    page.wait_for_timeout(3000)


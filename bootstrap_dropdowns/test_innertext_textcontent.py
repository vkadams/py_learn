from playwright.sync_api import Page, expect

def test_compare_methods(page: Page):
    page.goto('https://demowebshop.tricentis.com/')
    products = page.locator('.product-title')

    # inner_text() vs text_content()
    # print('Inner Text method:',products.nth(0).inner_text()) # no spaces - returns actual text
    # print('Text Content method:',products.nth(0).text_content()) # contains spaces before after
    for i in range(products.count()):
        #print('Inner Text method:', products.nth(i).inner_text())
        print('Text Content method:', products.nth(i).text_content().strip())

    # all_text_contents() vs all_inner_texts()
    #print(products.all_text_contents())
    print(products.all_inner_texts())

    # all() method - converting locator type to list we can use all method
    products_list = products.all()
    print('first product:',products_list[0].inner_text())

    for prod in products_list:
        print(prod.inner_text())



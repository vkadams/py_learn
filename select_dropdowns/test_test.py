from playwright.sync_api import Page, expect
import pytest

def test_sorting(page: Page):
    page.goto('https://bstackdemo.com/')

    # sort drop down is enabled or not
    expect(page.locator('div.sort select')).to_be_enabled()
    #page.locator('div.sort select').click()

    # sort by lowest to highest
    page.locator('div.sort select').select_option(value="lowestprice")
    page.wait_for_timeout(3000)
    all_product_names = [text.strip() for text in page.locator('p.shelf-item__title').all_text_contents()]
    #print(all_product_names)

    all_products_price = [text.strip() for text in page.locator('div.val').all_text_contents()]
    #print(all_products_price)

    # printing all product names & respective price
    for product, price in zip(all_product_names, all_products_price):
        print(f'The product name is {product} and price is {price}')

    # print highest priced & lowest priced products
    max_price = float('-inf')
    min_price = float('inf')
    highest_priced_product = None
    lowest_priced_product = None
    for product, price in zip(all_product_names, all_products_price):
        price = float(price.split('$')[1])

        if price > max_price:
            max_price = price
            highest_priced_product = product

        if price < min_price:
            min_price = price
            lowest_priced_product = product

    print(f'The highest priced product name is {highest_priced_product} and price is {max_price}')
    print(f'The lowest priced product name is {lowest_priced_product} and price is {min_price}')


    #page.wait_for_timeout(2000)
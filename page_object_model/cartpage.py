from playwright.sync_api import Page

class CartPage:
    def __init__(self, page):
        self.page = page
        # get all product names in the cart page
        self.product_names_locator = '#tbodyid tr td:nth-child(2)'

    def check_product_in_cart(self, product_name):
        products = self.page.locator(self.product_names_locator)

        for i in range(products.count()):
            name = products.nth(i).inner_text().strip()
            print(name)
            if name == product_name:
                return products.nth(i) # returning product

        return None

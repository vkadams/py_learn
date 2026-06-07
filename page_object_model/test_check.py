import pytest
from playwright.sync_api import Page

from loginpage import LoginPage

@pytest.mark.parametrize("username, password, product_name", [
    ("pavanol", "test@123", "Samsung galaxy s6")
])
def test_sample(page: Page, username, password, product_name):
    page.goto('https://demoblaze.com')

    login_page = LoginPage(page)
    login_page.perform_login(username, password)

    products_list = page.locator('div#tbodyid div.card h4.card-title a')
    #print(products_list)
    page.wait_for_timeout(5000)
    count = products_list.count()
    for i in range(count):
        name = products_list.nth(i).inner_text().strip()
        if name == product_name:
            print(name)
            products_list.nth(i).click()
            break
    page.wait_for_timeout(5000)



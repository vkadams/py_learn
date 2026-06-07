import pytest
from playwright.sync_api import Page, expect
# we need to import class, that's when we can create object & use the action methods
from loginpage import LoginPage
from homepage import HomePage
from cartpage import CartPage

@pytest.mark.parametrize("username, password, product_name", [
    ("pavanol", "test@123", "Samsung galaxy s6")
])
def test_user_can_login_and_add_product_to_cart(page: Page, username, password, product_name):
    page.goto('https://demoblaze.com/')

    # login
    login_page = LoginPage(page)
    login_page.click_login_link()
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login_button()

    # homepage
    home_page = HomePage(page)
    page.wait_for_timeout(3000)
    home_page.add_product_to_cart(product_name)
    page.wait_for_timeout(3000)
    home_page.goto_cart()
    page.wait_for_timeout(3000)

    # cartpage
    cart_page = CartPage(page)
    product_in_cart = cart_page.check_product_in_cart(product_name)

    # validations/expectations
    expect(product_in_cart).to_be_visible()



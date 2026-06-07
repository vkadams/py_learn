import pytest
from playwright.sync_api import Page, expect
import json

# since the test data is in json format
# import json & then open json, then load
file = open(r"C:\Users\61015706\OneDrive - LTIMindtree\Documents\PY\PPY\test_data\data.json","r")
login_data = json.load(file) # login_data contains entire data from json file

# for reading data from json we use for loop
@pytest.mark.parametrize("email, password, validity", [
    (data["email"],data["password"], data["validity"]) for data in login_data
])
def test_login_json_datadriven(email, password, validity, page: Page):
    # login form
    page.goto("https://demowebshop.tricentis.com/login")
    page.locator('#Email').fill(email)
    page.locator('#Password').fill(password)
    page.locator('input[value="Log in"]').click()

    # validation
    if validity == "valid":
        expect(page.locator('.ico-logout')).to_be_visible(timeout=5000)  # logout link
    else:
        expect(page.locator(".validation-summary-errors")).to_be_visible(timeout=5000)
        expect(page).to_have_url("https://demowebshop.tricentis.com/login")
import pytest
from playwright.sync_api import Page, expect
import csv

# since the test data is in csv format
# import csv & ensure open parameters newline, encoding
login_data = []
file = open(r"C:\Users\61015706\OneDrive - LTIMindtree\Documents\PY\PPY\test_data\data.csv",newline='',encoding="utf-8")
reader = csv.DictReader(file) # each row will be read as dictionary
for row in reader: # reader contains columns
    login_data.append((row["email"], row["password"], row["validity"]))

# for reading data from json we use for loop
@pytest.mark.parametrize("email, password, validity", login_data)
def test_login_csv_datadriven(email, password, validity, page: Page):
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
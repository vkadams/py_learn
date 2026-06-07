from playwright.sync_api import Page, expect
import pytest

def test_multi_select_dropdown(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # by using labels - list collection
    #page.locator('#colors').select_option(["Red", "Green", "White"]) # labels in list

    # by using values
    #page.locator('#colors').select_option(value=["white", "yellow", "green"])

    # by using index
    page.locator('#colors').select_option(index=[4, 2])

    # count number of options
    options = page.locator('#colors option')
    expect(options).to_have_count(7)

    # get option text in list
    print([txt.strip() for txt in page.locator('#colors option').all_text_contents()])

    # get individual text
    for text in page.locator('#colors option').all_text_contents():
        print(text.strip())




    page.wait_for_timeout(3000)
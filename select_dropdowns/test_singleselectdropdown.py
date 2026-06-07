from playwright.sync_api import Page, expect
import pytest

'''
3 ways to select dropdown-
by label
by value attribute
by index position
'''

def test_single_select_dropdown(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # using label-- most preferred as label will always be available
    # selecting by label one of them can be used-
    #page.locator('#country').select_option('India')
    page.locator('#country').select_option(label='India')

    # using value attribute
    page.locator('#country').select_option(value="germany") # simply "germany" can be used

    # using index
    page.locator('#country').select_option(index=6) # index starts from zero
    expect(page.locator('#country')).to_have_value('japan')

    # check number of options in dropdown
    dropdown_options = page.locator('#country option')
    expect(dropdown_options).to_have_count(10)

    # capturing option texts
    dropdown_texts = dropdown_options.all_text_contents() # list collection
    print([txt.strip() for txt in dropdown_options.all_text_contents()]) # list

    # printing individual values in the list
    for text in dropdown_texts:
        print(text.strip())

    page.wait_for_timeout(3000)

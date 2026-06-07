from playwright.sync_api import Page, expect
import pytest

def test_inputbox(page: Page):
    page.goto('https://testautomationpractice.blogspot.com/')
    name_input = page.locator('#name')
    expect(name_input).to_be_visible()
    expect(name_input).to_be_enabled()
    # check attribute of this element
    expect(name_input).to_have_attribute('maxlength','15')
    # get attribute of this element
    name_maxlength = name_input.get_attribute('maxlength')
    print('max length attribute value:',name_maxlength)
    # we can use pytest assertion
    assert name_maxlength == '15'
    # filling text
    name_input.fill('test-name')
    # capturing the value from this input box
    entered_name = name_input.input_value()
    print(entered_name)
    page.wait_for_timeout(3000)
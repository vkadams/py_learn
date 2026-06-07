from playwright.sync_api import Page, expect

def test_keyboard_actions(page: Page):
    page.goto('https://testautomationpractice.blogspot.com/')
    input1 = page.locator("#input1")
    # 1 - focus on input1
    input1.focus()
    # 2 - provide text using keyboard
    page.keyboard.insert_text("Hello World")
    # 3 - ctrl+a
    page.keyboard.press("Control+A")
    # 4 - ctrl+c
    page.keyboard.press("Control+C")
    # 5 - go to next field using tab key twice
    page.keyboard.press("Tab")
    page.keyboard.press("Tab")
    # 6 - paste the text ctrl+v
    page.keyboard.press("Control+V")

    # copy the same to next field
    page.keyboard.press("Tab")
    page.keyboard.press("Tab")
    page.keyboard.press("Control+V")

    input2 = page.locator("#input2")
    input3 = page.locator("#input3")

    expect(input2).to_have_value("Hello World")
    expect(input3).to_have_value("Hello World")

    page.wait_for_timeout(3000)


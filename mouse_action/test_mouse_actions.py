import pytest
from playwright.sync_api import Page, expect
@pytest.mark.skip()
def test_mouse_hover(page: Page):
    page.goto('https://testautomationpractice.blogspot.com/')
    pointme_button = page.locator('.dropbtn')
    pointme_button.hover()
    # select laptop-
    laptop = page.locator(".dropdown-content a").nth(1)
    laptop.hover()

    page.wait_for_timeout(3000)

@pytest.mark.skip()
def test_mouse_right_click(page: Page):
    page.goto('https://swisnl.github.io/jQuery-contextMenu/demo.html')
    button = page.locator(".context-menu-one.btn.btn-neutral")
    button.click(button="right") # to perform right click action

    page.wait_for_timeout(3000)

@pytest.mark.skip()
def test_mouse_double_click(page: Page):
    page.goto('https://testautomationpractice.blogspot.com/')
    btn_cpy = page.locator('button[ondblclick="myFunction1()"]')
    btn_cpy.dblclick() # performs double click
    field2 = page.locator("#field2")
    expect(field2).to_have_value("Hello World!")


    page.wait_for_timeout(3000)


def test_mouse_drag_drop(page: Page):
    page.goto('https://testautomationpractice.blogspot.com/')
    source = page.locator("#draggable")
    target = page.locator("#droppable")

    # approach 1- manually using hover+click
    # source.hover()
    # page.mouse.down()
    # target.hover()
    # page.mouse.up()

    # approach 2 - using dragto method-- preferred
    source.drag_to(target)


    page.wait_for_timeout(3000)

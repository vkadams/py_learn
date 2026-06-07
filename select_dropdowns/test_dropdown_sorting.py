from playwright.sync_api import Page, expect
import pytest

def test_multi_select_dropdown(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    colors_dropdown = page.locator("#colors option")
    colors_list = [text.strip() for text in colors_dropdown.all_text_contents()]
    original_list = colors_list.copy()
    the_sorted_colorlist = sorted(colors_list)
    print("The original list of colors: ",original_list)
    print("The sorted list of colors:",the_sorted_colorlist)
    if(original_list == the_sorted_colorlist):
        print('Colors dropdown options are in sorted order')
    else:
        print('Colors dropdown options are not in sorted order')


    animals_dropdown = page.locator("#animals option")
    animals_list = [text.strip() for text in animals_dropdown.all_text_contents()]
    original_animals_list = animals_list.copy()
    print("The original list of animals: ",original_animals_list)
    sorted_animals_list = sorted(animals_list)
    print("The sorted list of animals: ",sorted_animals_list)
    if(original_animals_list == sorted_animals_list):
        print('Animals dropdown options are in sorted order')
    else:
        print('Animals dropdown options are not in sorted order')
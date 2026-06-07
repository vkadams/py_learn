# pytest is required for data driven testing
import pytest
from playwright.sync_api import Page, expect

# data can in collections-- list/dict/set/tuples
search_items = ['laptop', 'Gift Card', 'smartphone', 'monitor']

# to parameterize to search multiple terms use pytest mark
# @pytest.mark.parametrize('item', ['laptop', 'Gift Card', 'smartphone', 'monitor'])
@pytest.mark.parametrize('search_item', search_items)
def test_search_items(search_item, page: Page):
    page.goto("https://demowebshop.tricentis.com/")
    page.locator("#small-searchterms").fill(search_item)
    page.locator('input[value="Search"]').click()

    # assertion - grab at-least one product info from search result
    first_result = page.locator('h2 a').nth(0)
    expect(first_result).to_contain_text(search_item, ignore_case=True)

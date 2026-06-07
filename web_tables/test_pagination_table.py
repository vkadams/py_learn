from playwright.sync_api import Page, expect

def test_pagination_table(page: Page):
    page.goto('https://datatables.net/examples/basic_init/zero_configuration.html')

    '''
    the case is that we do not know how many pages are there to be paginated
    so we can use while loop and not for loop
    '''
    page.wait_for_timeout(3000)
    has_more_pages = True
    while has_more_pages: # while this is true we need to read rows from table
        rows = page.locator('#example tbody tr').all()
        for row in rows:
            print(row.inner_text())
        page.wait_for_timeout(2000)
            # after reading each rows, need to click on next page button
        next_button = page.locator('button[data-dt-idx="next"]')
        next_is_disabled = next_button.get_attribute("class")
        if "disabled" in next_is_disabled:
            has_more_pages = False # we are at end of page.
        else:
            next_button.click() # proceed clicking on next page


def test_filter_rows(page: Page):
    page.goto('https://datatables.net/examples/basic_init/zero_configuration.html')
    dropdown = page.locator('#dt-length-0')
    dropdown.select_option(label='25')
    rows = page.locator('#example tbody tr')
    expect(rows).to_have_count(25)


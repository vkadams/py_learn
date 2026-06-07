from playwright.sync_api import Page, expect
import re

def test_dynamic_table(page: Page):
    page.goto('https://practice.expandtesting.com/dynamic-table')
    # For Chrome process get value of CPU load. Compare it with value in the yellow label.

    # capture table
    table = page.locator('table.table-striped tbody')
    rows = table.locator('tr').all() # get all rows & use all() to convert to list format
    cpu_load=""
    for row in rows:
        first_row = row.locator('td').nth(0).inner_text()
        if first_row == 'Chrome':
            cpu_load = row.locator('td:has-text("%")').inner_text()
            print(f'CPU load of {first_row} is {cpu_load}')
            break

    expect(page.locator("#chrome-cpu")).to_contain_text(cpu_load)


def test_another_dynamic_table(page: Page):
    page.goto('https://testautomationpractice.blogspot.com/')
    page.wait_for_timeout(3000)
    # get Memory Size of Firefox process:
    table = page.locator("#rows")
    rows = table.locator('tr').all()

    process = ""
    #page.wait_for_timeout(3000)
    for row in rows:
        brow_name = row.locator('td').nth(0).inner_text()
        if brow_name == 'Firefox':
            process = row.locator('td', has_text=re.compile('MB$')).inner_text()
            print(f'Memory Size of {brow_name} is {process}')
            break

    # mem_size = page.locator('.firefox-memory').inner_text()
    # print(mem_size)

    expect(page.locator('.firefox-memory')).to_contain_text(process)

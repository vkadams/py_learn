from playwright.sync_api import Page, expect

def test_book_flight(page: Page):
    page.goto('https://blazedemo.com/')
    departure = page.locator('select[name="fromPort"]')
    destination = page.locator('select[name="toPort"]')

    # selecting departure city & destination city
    departure.select_option("Boston")
    destination.select_option("Rome")
    page.locator('input[value="Find Flights"]').click()

    # click on choose flight having cheapest price
    flights_table = page.locator('.table tbody')
    rows = flights_table.locator('tr')
    row_count = rows.count()
    dollar_amts = list()
    lowest_price = ""
    for row in rows.all():
        prices = row.locator('td').nth(-1).all_inner_texts()
        for price in prices:
            dollar_amt = price.split('$')
            dollar_amts.append(dollar_amt[1])
    print(dollar_amts)

    sorted_dollar_amts = sorted(dollar_amts)
    lowest_price = '$'+sorted_dollar_amts[0]
    print('The lowest price is:',lowest_price)

    for i in range(row_count):
        if rows.nth(i).locator('td').nth(-1).inner_text() == lowest_price:
            rows.nth(i).locator('input[value="Choose This Flight"]').click()
            break





    page.wait_for_timeout(2000)
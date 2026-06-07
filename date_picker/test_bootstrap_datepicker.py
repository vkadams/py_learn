from playwright.sync_api import Page, expect

def select_checkin_date(page, year, month, date):
    while True:
        checkin_month_year = page.locator('h3.e7addce19e.af236b7586').nth(0).inner_text()
        current_month, current_year = checkin_month_year.split(' ')

        if current_month == month and current_year == year:
            break
        else:
            page.locator('button[aria-label="Next month"] span[class="fc70cba028 e2a1cd6bfe"] svg').click()


    all_dates = page.locator('table.b8fcb0c66a tbody').nth(0).locator('td').all()
    for dt in all_dates:
        if dt.inner_text() == date:
            dt.click()
            break

def select_checkout_date(page, year, month, date):
    while True:
        checkin_month_year = page.locator('h3.e7addce19e.af236b7586').nth(1).inner_text()
        current_month, current_year = checkin_month_year.split(' ')

        if current_month == month and current_year == year:
            break
        else:
            page.locator('button[aria-label="Next month"] span[class="fc70cba028 e2a1cd6bfe"] svg').click()

    all_dates = page.locator('table.b8fcb0c66a tbody').nth(1).locator('td').all()
    for dt in all_dates:
        if dt.inner_text() == date:
            dt.click()
            break


def test_booking_datepicker(page: Page):
    page.goto('https://www.booking.com/')
    page.wait_for_timeout(3000)
    if page.locator('div.b779265b5e button[type="button"]').is_enabled():
        page.locator('div.b779265b5e button[type="button"]').click()

    page.get_by_test_id("date-display-field-start").click() # click on date picker
    select_checkin_date(page, "2026", "October", "10")
    select_checkout_date(page, "2026", "November", "5")
    checkin_text = page.locator('span[data-testid="date-display-field-start"]').inner_text()
    checkout_text = page.locator('span[data-testid="date-display-field-end"]').inner_text()
    print('Check in date==>',checkin_text, 'Check out date==>',checkout_text)

    expect(page.locator('span[data-testid="date-display-field-start"]')).to_contain_text(checkin_text)
    expect(page.locator('span[data-testid="date-display-field-end"]')).to_contain_text(checkout_text)

    page.wait_for_timeout(3000)
from playwright.sync_api import Page, expect

def select_date(page, target_date, target_month, target_year, future_date):
    # selecting month & year
    while True:
        current_month = page.locator('.ui-datepicker-month').inner_text()
        current_year = page.locator('.ui-datepicker-year').inner_text()

        if current_month == target_month and current_year == target_year:
            break # we do not want to navigate
        if future_date == True:
            page.locator('.ui-icon.ui-icon-circle-triangle-e').click() # future date
        else:
            page.locator('.ui-icon.ui-icon-circle-triangle-w').click() # past date

    # selecting "date" from date picker
    page.wait_for_timeout(3000)
    all_dates = page.locator('.ui-datepicker-calendar tbody tr td').all()
    for dt in all_dates:
        date_text = dt.inner_text()
        if date_text == target_date:
            dt.click()
            break


def test_jquery_datepicker(page:Page):
    page.goto('https://testautomationpractice.blogspot.com/')
    # wheneverthere is input tag its usually jquery field can use fill method
    date_input = page.locator('#datepicker')
    # approach 1
    # date_input.fill('10/15/2026') # mm/dd/yy
    # expect(date_input).to_have_value('10/15/2026')

    # approach 2- using user define function
    future_date = False # future date or past date
    month = "July"
    date = "2"
    year = "2024"

    date_input.click() # opens the date picker
    select_date(page, date, month, year, future_date)
    print(date_input.input_value())
    # we need to implement this outside of test function

    expect(date_input).to_have_value("07/02/2024")


    page.wait_for_timeout(3000)

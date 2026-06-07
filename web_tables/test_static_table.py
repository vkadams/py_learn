from playwright.sync_api import Page, expect

def test_static_table(page: Page):
    page.goto('https://testautomationpractice.blogspot.com/')
    # locate table
    table = page.locator('table[name="BookTable"] tbody')
    expect(table).to_be_visible()

    # count number of rows in this table
    rows = table.locator('tr')
    expect(rows).to_have_count(rows.count())
    print('Number of rows in the table', rows.count())

    # count number of headers in the table
    columns = rows.locator('th')
    expect(columns).to_have_count(columns.count())
    print('Number of columns in the table', columns.count())

    # read data from second row of the table excluding header
    second_row_cells = rows.nth(2).locator('td')
    second_row_texts = second_row_cells.all_inner_texts()
    print('second row data',second_row_texts)
    expect(second_row_cells).to_have_text(['Learn Java', 'Mukesh', 'Java', '500'])

    for text in second_row_texts:
        print(text)


    # read all the data from the table excluding header
    all_row_data = rows.all()
    for row in all_row_data[1:]: # excluding header row so slice 1:
        cols = row.locator('td').all_inner_texts()
        print(cols)

    # print book names where author name is Mukesh
    for row in all_row_data[1:]:
        auth_name = row.locator('td').nth(1).inner_text()
        if auth_name == 'Mukesh':
            book_name = row.locator('td').nth(0).inner_text()
            print(f'{auth_name}\t{book_name}')


    # find total prices of all books
    total_price = 0
    for row in all_row_data[1:]:
        price = row.locator('td').nth(-1).inner_text()
        #print(price)
        total_price = total_price + int(price)
    print('The total price is:',total_price)



    #page.wait_for_timeout(3000)
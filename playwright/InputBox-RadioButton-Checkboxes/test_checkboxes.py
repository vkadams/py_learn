from playwright.sync_api import Page, expect
import pytest

def test_inputbox(page: Page):
    page.goto('https://testautomationpractice.blogspot.com/')

    # select specific checkbox- say Sunday
    sunday_chckbox = page.get_by_label('Sunday')
    sunday_chckbox.check()
    expect(sunday_chckbox).to_be_checked()

    # count total number of checkboxes
    '''
    using selector page.locator('input[id$="day"]'), we can select all checkboxes
    only that it will return locator/return type is locator
    to get this into a list, so that it is iterable
    get all labels into a list
    '''
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    checkboxes = []
    for day in days:
        checkbox = page.get_by_label(day)
        checkboxes.append(checkbox)
    print('Number of checkboxes:',len(checkboxes))


    # check all the checkboxes
    # for checkbox in checkboxes:
    #     if not checkbox.is_checked():
    #         checkbox.check()
    # expect(checkbox).to_be_checked()

    # uncheck only last 3 checkboxes
    # last_three = checkboxes[-3:]
    # for checkbox in last_three:
    #     checkbox.uncheck()
    # expect(checkbox).not_to_be_checked()

    # uncheck those selected & check those are not selected-- toggle checkboxes
    # for checkbox in checkboxes:
    #     if checkbox.is_checked():
    #         checkbox.uncheck()
    #         expect(checkbox).not_to_be_checked()
    #     else:
    #         checkbox.check()
    #         expect(checkbox).to_be_checked()


    # randomly check checkboxes-- 1,3,6
    # indexes = [1,3,6]
    # for index in indexes:
    #     checkboxes[index].check()
    #     expect(checkboxes[index]).to_be_checked()

    # select checkbox based on label
    weekday_chkbox = 'Friday'
    for label in days:
        if label == weekday_chkbox:
            checkbox = page.get_by_label(label)
            checkbox.check()
            expect(checkbox).to_be_checked()




    page.wait_for_timeout(3000)
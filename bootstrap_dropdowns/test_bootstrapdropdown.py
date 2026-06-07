from playwright.sync_api import Page, expect
import pytest

def test_bootstrapdropdown(page: Page):
    # login
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").fill("admin123")
    page.get_by_role('button', name='Login').click()
    page.wait_for_timeout(3000)

    # click on PIM
    page.get_by_text('PIM').click()
    page.wait_for_timeout(8000)

    # click on job title dropdown
    page.locator('form i').nth(2).click() # this opens available options
    page.wait_for_timeout(3000)
    #*** to get options using selectorshub
    '''
    open selectors hub
    click turn on debugger icon-- immediately click on dropdown
    screen will be in pause mode
    go to elements
    & start inspecting elements
    '''
    options = page.locator("div[role='listbox'] span")
    expect(options).to_have_count(options.count())
    # once locator is captured, click on resume script execution to return to normal stage
    job_titles_dropdown = [text for text in page.locator("div[role='listbox'] span").all_text_contents()]
    print(job_titles_dropdown)
    print('Number of job titles in the dropdown:',len(job_titles_dropdown))
    # printing individually-
    for title in job_titles_dropdown:
        print(title)

    #*** to get options using dev tools
    '''
    dev tools> sources> open the dropdown
    click on pause
    proceed inspecting elements
    '''

    # select/click on specific option
    for i in range(options.count()):
        text = options.nth(i).text_content()
        if text == 'Finance Manager':
            options.nth(i).click()
            break

    
    page.wait_for_timeout(3000)
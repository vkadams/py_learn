from playwright.sync_api import Page

def test_flipkart_search(page: Page):
    page.goto('https://www.flipkart.com/')
    page.wait_for_timeout(2000)
    if page.locator('.q7ywiQ').is_visible():
        page.get_by_role('button', name='✕').click()
        #page.locator('span.b3wTlE').click()

    page.wait_for_timeout(2000)

    search_bar = page.locator('input[name="q"]').first
    search_bar.fill('smart')
    page.wait_for_timeout(3000)

    suggestions = page.locator('li.Swx5kP')
    print('suggestions count:',suggestions.count())

    suggestions_list = suggestions.all_inner_texts()
    print('All suggestions:',suggestions_list)

    print('The third suggestion:', suggestions.nth(2).inner_text())

    for i in range(suggestions.count()):
        suggestion = suggestions.nth(i).inner_text().strip()
        if suggestion == 'smartphone':
            suggestions.nth(i).click()
            break

    page.wait_for_timeout(3000)
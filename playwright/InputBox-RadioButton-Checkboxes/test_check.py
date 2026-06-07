from playwright.sync_api import Page, expect
import pytest

def test_checks(page: Page):
    page.goto('https://practice-automation.com/form-fields/')
    #page.get_by_test_id('name-input').fill('John')
    #page.get_by_label('Password').fill('password')

    drinks = ['Water', 'Milk', 'Coffee', 'Wine', 'Ctrl-Alt-Delight']
    labels = []
    for drink in drinks:
        label = page.get_by_label(drink)
        labels.append(label)
    print(len(labels))

    for label in labels:
        label.check()
        expect(label).to_be_checked()

    for label in labels[-2:]:
        label.uncheck()
        expect(label).not_to_be_checked()

    page.wait_for_timeout(3000)
import pytest
from playwright.sync_api import Page, expect

@pytest.mark.skip()
def test_upload_singlefile(page: Page):
    page.goto('https://testautomationpractice.blogspot.com/')
    page.locator("#singleFileInput").set_input_files(r"C:\Users\61015706\OneDrive - LTIMindtree\Documents\PY\PPY\uploads\test1.txt")

    page.locator('button:has-text("Upload Single File")').click()
    expect(page.locator("#singleFileStatus")).to_contain_text("test1.txt")
    print("File upload successful")
    page.wait_for_timeout(3000)


def test_upload_multiplefiles(page: Page):
    page.goto('https://testautomationpractice.blogspot.com/')
    #files = [r"C:\Users\61015706\OneDrive - LTIMindtree\Documents\PY\PPY\uploads\test1.txt", r"C:\Users\61015706\OneDrive - LTIMindtree\Documents\PY\PPY\uploads\test1 - Copy.txt"]

    files1 = ["uploads/test1.txt", "uploads/test1 - Copy.txt"]
    page.locator("#multipleFilesInput").set_input_files(files1)

    page.locator('button:has-text("Upload Multiple Files")').click()
    expect(page.locator("#multipleFilesStatus")).to_contain_text("test1.txt")
    expect(page.locator("#multipleFilesStatus")).to_contain_text("test1 - Copy.txt")
    print("File upload successful")
    page.wait_for_timeout(3000)
import pytest
import os
from playwright.sync_api import Page, expect

def test_file_download(page:Page):
    page.goto('https://testautomationpractice.blogspot.com/p/download-files_25.html')

    page.locator("#inputText").fill("Hello World") # fill the text field
    page.locator("#generateTxt").click() # click the generate link link

    # this is an event so we need to register this event- download event
    page.on("download", lambda download:download.save_as("downloads/save.txt"))
    page.locator("#txtDownloadLink").click() # click to download

    page.wait_for_timeout(3000)
    if os.path.exists('downloads/save.txt'):
        print("File exists")
    else:
        print("File does not exist")

    page.wait_for_timeout(2000)

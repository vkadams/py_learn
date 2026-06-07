from playwright.sync_api import Playwright, expect, Page
import time
import datetime

def test_screenshot_demo(page:Page):
    page.goto("https://demowebshop.tricentis.com/")
    #timestamp = str(int(time.time()))
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

    # page screenshot
    #page.screenshot(path=f"screenshots/homepage_{timestamp}.png")

    # full page screenshot
    #page.screenshot(path=f"screenshots/homepage_{timestamp}.png", full_page=True)

    # element screenshot
    prod_grid = page.locator('.product-grid.home-page-product-grid')
    prod_grid.screenshot(path=f"screenshots/homepage_{timestamp}.png")

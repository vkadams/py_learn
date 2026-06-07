# importing page fixture is step 1
import pytest
from playwright.async_api import async_playwright, Page, expect

# this is not needed, we would not use async mode for web automation
# will need to use for api testing- where we wait for api to respond to proceed

@pytest.mark.asyncio
async def test_verifypageurl():
    async with async_playwright() as page:
        browser = await page.chromium.launch(headless=False)
        mypage = await browser.new_page()
        await mypage.goto('https://automationexercise.com/')
        await expect(mypage).to_have_url('https://automationexercise.com/')


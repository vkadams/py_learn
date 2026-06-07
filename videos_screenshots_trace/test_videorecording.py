from playwright.sync_api import Playwright, expect
import os

def test_record_video(playwright: Playwright):
    video_path = r"C:\Users\61015706\OneDrive - LTIMindtree\Documents\PY\PPY\videos"

    if not os.path.exists(video_path):
        os.makedirs(video_path)

    browser = playwright.chromium.launch(headless=True)

    context = browser.new_context(
        record_video_dir=video_path,
        record_video_size={"width": 1280, "height": 720}
    )
    #print(context._options)

    page = context.new_page()

    page.goto("https://demoblaze.com/")
    page.locator('#login2').click()
    page.locator('#loginusername').fill("pavanol")
    page.locator('#loginpassword').fill("test@123")
    page.locator('button[onclick="logIn()"]').click()

    page.wait_for_timeout(3000)

    expect(page.locator('#logout2')).to_be_visible()
    expect(page.locator('#nameofuser')).to_contain_text('Welcome pavanol')
    page.wait_for_timeout(3000)
    # ✅ Important
    page.close()
    #print(page.video)
    context.close()
    #print(page.video.path())
    browser.close()

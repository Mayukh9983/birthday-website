
from playwright.sync_api import sync_playwright
import os

def verify_changes():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        # Open the local file directly using absolute path
        cwd = os.getcwd()
        page.goto(f"file://{cwd}/index.html")

        # Verify images have loading="lazy"
        images = page.locator(".gallery-container img").all()
        print(f"Found {len(images)} images")

        for i, img in enumerate(images):
            loading = img.get_attribute("loading")
            width = img.get_attribute("width")
            height = img.get_attribute("height")
            print(f"Image {i+1}: loading={loading}, width={width}, height={height}")
            if loading != "lazy":
                print("FAIL: loading attribute missing or incorrect")
            if width != "300" or height != "300":
                print("FAIL: width/height missing or incorrect")

        page.screenshot(path="verification/verification.png")

        browser.close()

if __name__ == "__main__":
    verify_changes()

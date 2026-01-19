
from playwright.sync_api import sync_playwright

def verify_changes():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://localhost:8080/index.html")

        # Verify script.js is NOT loaded
        # We can check if the script tag with src="js/script.js" exists
        script_tag = page.locator('script[src="js/script.js"]')
        count = script_tag.count()
        if count == 0:
            print("SUCCESS: script.js is not present.")
        else:
            print("FAILURE: script.js IS present.")

        # Verify images have loading="lazy"
        # Since images are hidden initially, we can still check attributes
        images = page.locator('.gallery-container img')
        count_images = images.count()
        print(f"Found {count_images} images.")

        for i in range(count_images):
            img = images.nth(i)
            loading_attr = img.get_attribute("loading")
            width_attr = img.get_attribute("width")
            height_attr = img.get_attribute("height")

            if loading_attr == "lazy":
                print(f"Image {i+1}: loading='lazy' present.")
            else:
                print(f"Image {i+1}: loading='lazy' MISSING. Found: {loading_attr}")

            if width_attr == "300" and height_attr == "300":
                 print(f"Image {i+1}: width/height attributes correct.")
            else:
                 print(f"Image {i+1}: width/height attributes MISSING or incorrect. Found: {width_attr}x{height_attr}")

        # Take a screenshot just to be safe, although visual changes are minimal (width/height might affect layout slightly before css loads)
        # But since CSS loads fast locally, we might not see it.
        # We'll force the gallery to be visible for the screenshot
        page.evaluate("document.querySelector('.photo-gallery').style.opacity = '1'")
        page.evaluate("document.querySelector('.photo-gallery').style.animation = 'none'")

        page.screenshot(path="verification/verification.png")
        print("Screenshot saved to verification/verification.png")

        browser.close()

if __name__ == "__main__":
    verify_changes()

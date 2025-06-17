# scraping/scraper.py

from playwright.sync_api import sync_playwright
import os

RAW_PATH = os.path.join("data", "raw")


def scrape_chapter(url):
    os.makedirs(RAW_PATH, exist_ok=True)
    
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)

        html = page.inner_text("body")        
        
        # Save screenshot with timestamp
        screenshot_path = os.path.join(RAW_PATH, "chapter_screenshot.png")
        page.screenshot(path=screenshot_path, full_page=True)

        # Save screenshot
        page.screenshot(path=os.path.join(RAW_PATH, "chapter.png"))
        # Save text
        with open(os.path.join(RAW_PATH, "chapter.txt"), "w", encoding="utf-8") as f:
            f.write(html)

        browser.close()

        return html
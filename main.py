from playwright.sync_api import sync_playwright

def scrape_aviator():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.sportybet.com/ng/aviator")
        page.wait_for_timeout(5000)
        multipliers = [round(1.0 + i * 0.05, 2) for i in range(30)]
        browser.close()
        return multipliers

if __name__ == "__main__":
    print(scrape_aviator())

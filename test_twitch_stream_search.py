import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_twitch_stream_search(driver):
    # 1. Go to Twitch mobile site
    driver.get("https://m.twitch.tv/")

    # 1.1 Accept Cookies if the banner appears
    wait = WebDriverWait(driver, 10)
    try:
        accept_cookies_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-a-target="consent-banner-accept"]')))
        accept_cookies_btn.click()
    except:
        print("No cookie banner found, proceeding...")

    # 2. Click on the search icon
    wait = WebDriverWait(driver, 10)
    search_icon = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-a-target="search-bar-icon-button"]')))
    search_icon.click()

    # 3. Input 'StarCraft II'
    search_box = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="search"]')))
    search_box.send_keys("StarCraft II")
    search_box.send_keys(Keys.RETURN)

    # 4. Scroll down 2 times
    time.sleep(2)  # Wait for search results to load
    for _ in range(2):
        driver.execute_script("window.scrollBy(0, 1000);")
        time.sleep(2)  # Wait for scroll effect and more content to load

    # 5. Select a streamer
    streamer = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-a-target="preview-card-channel-link"]')))
    streamer.click()

    # 6. Wait for the streamer's page to load completely and take a screenshot
    time.sleep(5)  # Wait for video elements to load (increase this time if needed)

    # Handle potential pop-ups/modals
    try:
        modal_close_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-a-target="consent-banner-accept"]')))
        modal_close_button.click()
    except:
        pass  # Modal might not always appear, safe to ignore if not found

    # Screenshot after page load
    driver.save_screenshot("twitch_streamer_page.png")
    print("Screenshot saved as twitch_streamer_page.png")
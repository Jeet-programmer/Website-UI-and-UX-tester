from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def links_to_screenshot(link):
# Initialize Chrome options
    print("Taking screenshot...")
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Run in headless mode
    chrome_options.add_argument("--disable-dev-shm-usage")
    # Initialize the WebDriver with Chrome options
    driver = webdriver.Chrome(options=chrome_options)

# Navigate to the webpage
    driver.get(link)

    # Wait for the full site to load (you may need to adjust the timeout)
    wait = WebDriverWait(driver, 5)  # Wait up to 5 seconds
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))  # Wait until <body> tag is present

    # Take a screenshot
    driver.save_screenshot("screenshot.png")

    # Close the browser
    driver.quit()
# links_to_screenshot("https://lumaticai.com/")
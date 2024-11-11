from webdriver_manager.chrome import ChromeDriverManager  # Add this import at the top
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from cookies import load_cookies, save_cookies, is_authenticated
from downloader import fetch_video_url, download_video_file
from authentication import authenticate_user
import os
import argparse
from dotenv import load_dotenv


def load_environment_variables():
    """Loads environment variables."""
    load_dotenv()
    school = os.getenv("SCHOOL")
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    if not all([school, username, password]):
        print("Error: Missing one or more environment variables.")
    return username, password, school

def setup_selenium_driver():
    """Sets up a headless Selenium WebDriver."""
    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def main(url, output_folder="downloads"):
    """Main function to execute the video download process."""
    username, password, school = load_environment_variables()

    # Set up Selenium WebDriver
    driver = setup_selenium_driver()

    try:
        driver.get(url)  # Open initial page

        # Load cookies if available and attempt access
        if load_cookies(driver):
            driver.get(url)
            if is_authenticated(driver):
                print("Authenticated with cookies.")
            else:
                print("Cookies invalid, proceeding with login...")
                authenticate_user(driver, url, username, password, school)
                save_cookies(driver)  # Save cookies after authentication
        else:
            # If no cookies found, authenticate
            print("No cookies found, proceeding with login...")
            authenticate_user(driver, url, username, password, school)
            save_cookies(driver)  # Save cookies after authentication

        # Fetch the video URL
        video_url = fetch_video_url(driver)

        # Download the video file if URL was found
        if video_url:
            download_video_file(video_url, driver, output_folder)
        else:
            print("Video URL not found. Exiting.")
    finally:
        driver.quit()

# Example usage
# if __name__ == "__main__":
#     video_page_url = "https://tube.switch.ch/videos/uxbITIynrz"
#     main(video_page_url)

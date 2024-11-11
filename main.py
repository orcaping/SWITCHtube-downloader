from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from cookies import load_cookies, save_cookies, is_authenticated
from downloader import fetch_video_url, download_video_file, folder_downloader
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

        # # Load cookies if available and attempt access
        # if load_cookies(driver):
        #     driver.get(url)
        #     if is_authenticated(driver):
        #         print("Authenticated with cookies.")
        #     else:
        #         print("Cookies invalid, proceeding with login...")
        #         authenticate_user(driver, url, username, password, school)
        #         save_cookies(driver)  # Save cookies after authentication
        # else:
        # If no cookies found, authenticate
        # print("No cookies found, proceeding with login...")
        authenticate_user(driver, url, username, password, school)
        # save_cookies(driver)  # Save cookies after authentication

        if "channels" in url:
            folder_downloader(url, driver)
        elif "videos" in url:
            video_url = fetch_video_url(driver)

            if video_url:
                download_video_file(video_url, driver, output_folder)
            else:
                print("Video URL not found. Exiting.")
        else:
            print("Invalid URL. Exiting.")
            return
    finally:
        driver.quit() 

# Example usage
if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Download videos from SWITCHtube.")
    parser.add_argument("url", help="URL of the video or folder to download.")
    args = parser.parse_args()
    main(args.url)    
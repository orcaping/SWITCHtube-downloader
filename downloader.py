import os
import requests
import pickle
from selenium.webdriver.common.by import By
from cookies import load_cookies, save_cookies


def fetch_video_url(driver):
    """Fetches the video URL from the loaded page source."""
    print("Waiting for the video page to load...")
    try:
        video_element = driver.find_element(By.XPATH, "//source[contains(@type, 'video/mp4')]")
        video_url = video_element.get_attribute("src")
        print(f"Found video URL: {video_url}")
        return video_url
    except Exception as e:
        print(f"Error locating video URL: {e}")
        return None


# WIP
def folder_downloader(folder_url, driver, output_folder="downloads"):
    """ Downloads all video files in a specified folder"""

    video_hrefs = []
    video_divs = driver.find_elements(By.XPATH, "//turbo-frame[@id='videos-items']//div[starts-with(@id, 'video_')]")
    
    for video in video_divs:
        a_element = video.find_element(By.TAG_NAME, 'a')
        href = a_element.get_attribute('href')
        video_hrefs.append(href)

    for href in video_hrefs:
        driver.get(href)
        video_url = fetch_video_url(driver)
        if os.path.exists(video_url):
            print(f"Video already exists: {video_url}")
            continue
        download_video_file(video_url, driver)
        driver.get(folder_url)


def download_video_file(video_url, driver, output_folder="downloads"):
    """Downloads the video file from the given URL."""

    save_cookies(driver)  # Save cookies for the requests session

    video_name = driver.find_element(By.XPATH, "//div[@class='title-with-menu']//h1[1]").text
    parent_dir = driver.find_element(By.XPATH, "//div[@class='title-with-menu']//div[@class='headers']//h2/a").text
    video_parentdir_name = parent_dir.replace(" ", "_")
    os.makedirs(os.path.join(output_folder, video_parentdir_name), exist_ok=True)
    video_filename = video_name.replace(", ", "-") + ".mp4"
    video_path = os.path.join(output_folder, video_parentdir_name, video_filename)

    if os.path.exists(video_path):
        print(f"Video already exists: {video_path}")
        return

    session = requests.Session()

    # Load cookies into requests session
    with open("cookies.pkl", "rb") as f:
        cookies = pickle.load(f)
        for cookie in cookies:
            session.cookies.set(cookie['name'], cookie['value'], domain=cookie['domain'])

    print(f"Downloading video from: {video_url}")
    response = session.get(video_url, stream=True)

    if response.status_code == 200:
        with open(video_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Video downloaded successfully: {video_path}")
    else:
        print(f"Failed to download video, status code: {response.status_code}")

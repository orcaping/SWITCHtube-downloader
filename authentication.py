from selenium.webdriver.common.by import By  # type: ignore
from selenium.webdriver.support.ui import WebDriverWait  # type: ignore
from selenium.webdriver.support import expected_conditions as EC  # type:ignore


def authenticate_user(driver, url, username, password, school):
    """Authenticates the user on the website."""
    print(f"Opening URL: {url}")
    driver.get(url)

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "userIdPSelection_iddtext"))
        ).send_keys(school)
        driver.find_element(By.NAME, "Select").click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        ).send_keys(username)
        driver.find_element(By.ID, "button-submit").click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "password"))
        ).send_keys(password)
        driver.find_element(By.ID, "button-proceed").click()
        print("User authenticated.")
    except Exception as e:
        print(f"Authentication failed: {e}")

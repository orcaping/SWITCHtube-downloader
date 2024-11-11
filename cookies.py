import os
import pickle
from selenium.webdriver.common.by import By  # type: ignore


def save_cookies(driver, filename="cookies.pkl"):
    """Save all cookies to a file."""
    with open(filename, "wb") as f:
        pickle.dump(driver.get_cookies(), f)
    print("Cookies saved.")


def load_cookies(driver, filename="cookies.pkl"):
    """Loads cookies into the driver."""
    if os.path.exists(filename):
        with open(filename, "rb") as f:
            cookies = pickle.load(f)
            for cookie in cookies:
                # Selenium requires domain without leading dot
                cookie['domain'] = cookie['domain'].lstrip(".")
                try:
                    driver.add_cookie(cookie)
                    print(f"Loaded cookie: {cookie['name']}")
                except Exception as e:
                    print(f"Failed to load cookie {cookie['name']}: {e}")
        return True
    print("No cookies found.")
    return False


def is_authenticated(driver):
    """Check if user is authenticated by looking for specific page elements."""
    try:
        driver.find_element(By.ID, "userIdPSelection_iddtext")
        return False  # If this element is present, authentication is required
    except Exception:
        return True

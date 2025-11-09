from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import WebDriverException
import logging

from config.settings import (
    USE_CHROME_PROFILE,
    CHROME_USER_DATA_DIR,
    HEADLESS,
)


def build_driver():
    chrome_options = webdriver.ChromeOptions()

    if USE_CHROME_PROFILE:
        if not CHROME_USER_DATA_DIR or "path/to" in CHROME_USER_DATA_DIR:
            logging.error("Please set CHROME_USER_DATA_DIR to your real Chrome user data directory.")
            raise SystemExit("CHROME_USER_DATA_DIR not configured.")

        chrome_options.add_argument(f"--user-data-dir={CHROME_USER_DATA_DIR}")

    if HEADLESS:
        chrome_options.add_argument("--headless=new")

    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")

    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
    except WebDriverException as e:
        logging.exception("Error creating Chrome driver: %s", e)
        raise

    driver.set_page_load_timeout(30)

    return driver

import logging
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from config.settings import LINKEDIN_EMAIL, LINKEDIN_PASSWORD
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def login_linkedin(driver):

    logging.info("Logging into LinkedIn...")

    driver.get("https://www.linkedin.com/login")

    try:
        email_input = driver.find_element(By.ID, "username")
        password_input = driver.find_element(By.ID, "password")

        email_input.send_keys(LINKEDIN_EMAIL)
        password_input.send_keys(LINKEDIN_PASSWORD)

        submit_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_btn.click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "global-nav"))
        )

        logging.info("Logged in successfully!")

    except (NoSuchElementException, TimeoutException) as e:
        logging.error(f"Login failed: {e}")
        raise SystemExit("Unable to login. Please check your credentials or captcha.")

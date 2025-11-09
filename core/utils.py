import logging
from pathlib import Path
from selenium.common.exceptions import NoSuchElementException

from config.settings import OUTPUT_DIR


def ensure_output_dir():
    Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)


def safe_text(element):
    try:
        text = element.text.strip()
        return text if text else None
    except Exception:
        return None


def element_text_or_none(driver, by, selector):
    try:
        el = driver.find_element(by, selector)
        return safe_text(el)
    except NoSuchElementException:
        return None

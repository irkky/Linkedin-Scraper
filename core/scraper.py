import re
import logging
import time
import random
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.settings import (
    MAX_WAIT,
    MIN_DELAY,
    MAX_DELAY
)

from core.utils import (
    safe_text,
    element_text_or_none,
)


def extract_profile(driver, url):
    data = {"url": url}

    try:
        driver.get(url)
    except Exception as e:
        logging.warning(f"Driver.get error for {url}: {e}")

    try:
        WebDriverWait(driver, MAX_WAIT).until(
            EC.presence_of_element_located((By.TAG_NAME, "main"))
        )
    except Exception:
        logging.warning("Timed out waiting for page to load. May need login/captcha.")

    data["name"] = element_text_or_none(driver, By.TAG_NAME, "h1")

    data["headline"] = (
        element_text_or_none(driver, By.CSS_SELECTOR, "div.text-body-medium")
        or element_text_or_none(driver, By.CSS_SELECTOR, "h2")
    )

    data["location"] = (
        element_text_or_none(driver, By.CSS_SELECTOR, "span.text-body-small.inline")
        or element_text_or_none(driver, By.CSS_SELECTOR, ".pv-top-card--list-bullet li")
    )

    about = None
    try:
        about_el = driver.find_element(
            By.XPATH,
            "//section//h2[contains(translate(., 'ABOUT', 'about'), 'about')]/following-sibling::*"
        )
        about = safe_text(about_el)
    except Exception:
        about = None

    data["about"] = about

    page_html = driver.page_source
    soup = BeautifulSoup(page_html, "html.parser")

    experiences = extract_experiences(soup, driver)
    education = extract_education(soup, driver)

    data["experiences"] = " ||| ".join(experiences) if experiences else None
    data["education"] = " ||| ".join(education) if education else None

    if not data["name"]:
        h1 = soup.find("h1")
        data["name"] = h1.get_text(strip=True) if h1 else None

    if not data["headline"]:
        meta = soup.find(lambda tag: tag.name in ["div", "span"] and tag.get_text(strip=True))
        data["headline"] = data["headline"] or (meta.get_text(strip=True) if meta else None)

    return data


def extract_experiences(soup, driver):
    experiences = []

    try:
        exp_section = soup.find(
            lambda tag: tag.name in ["section", "div"]
            and tag.get_text().lower().strip().startswith("experience")
        )

        if exp_section:
            items = exp_section.find_all(["li", "div"], recursive=True)
            for it in items:
                txt = it.get_text(" ", strip=True)
                if txt and len(txt) > 30 and not re.search(r"show more", txt, re.I):
                    experiences.append(txt)

    except Exception:
        pass

    if not experiences:
        try:
            nodes = driver.find_elements(
                By.CSS_SELECTOR,
                "section#experience-section li, section#experience-section .pv-entity__summary-info"
            )
            for el in nodes:
                t = safe_text(el)
                if t and len(t) > 20:
                    experiences.append(t)
        except Exception:
            pass

    return list(dict.fromkeys(experiences))


def extract_education(soup, driver):
    education = []

    try:
        edu_section = soup.find(lambda tag: "education" in (tag.get("id") or "").lower())

        if not edu_section:
            headings = soup.find_all(
                lambda tag: tag.name in ["h2", "h3", "span"] and "education" in tag.get_text().lower()
            )
            if headings:
                edu_section = headings[0].parent

        if edu_section:
            items = edu_section.find_all(["li", "div"], recursive=True)
            for it in items:
                txt = it.get_text(" ", strip=True)
                if txt and len(txt) > 20 and not re.search(r"show more", txt, re.I):
                    education.append(txt)

    except Exception:
        pass

    if not education:
        try:
            nodes = driver.find_elements(
                By.CSS_SELECTOR,
                "section#education-section li, section#education-section .pv-entity__degree-info"
            )
            for el in nodes:
                t = safe_text(el)
                if t and len(t) > 20:
                    education.append(t)
        except Exception:
            pass

    return list(dict.fromkeys(education))


def polite_delay():
    delay = random.uniform(MIN_DELAY, MAX_DELAY)
    logging.debug(f"Sleeping for {delay:.2f} seconds...")
    time.sleep(delay)

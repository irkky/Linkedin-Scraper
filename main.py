import logging
from core.driver_builder import build_driver
from core.scraper import extract_profile, polite_delay
from core.utils import ensure_output_dir
from data.io_handler import load_urls, save_profiles, save_normalized
from data.normalizer import normalize_list_to_rows
from core.login import login_linkedin
from config.settings import MAX_PROFILES


def main():
    ensure_output_dir()

    # Load URLs from Excel
    urls = load_urls()
    urls = urls[:MAX_PROFILES]
    logging.info(f"Processing {len(urls)} profile URLs")

    driver = build_driver()

    login_linkedin(driver)
    
    profile_results = []

    try:
        for idx, url in enumerate(urls, start=1):
            logging.info(f"[{idx}/{len(urls)}] Scraping: {url}")

            try:
                profile_data = extract_profile(driver, url)
                profile_results.append(profile_data)

            except Exception as e:
                logging.exception(f"Error scraping {url}: {e}")
                profile_results.append({"url": url, "error": str(e)})

            polite_delay()

    finally:
        try:
            driver.quit()
        except Exception:
            pass

    # Save main profiles
    save_profiles(profile_results)

    # Normalize and save experiences & education
    exp_rows, edu_rows = normalize_list_to_rows(profile_results)
    save_normalized(exp_rows, edu_rows)


if __name__ == "__main__":
    main()

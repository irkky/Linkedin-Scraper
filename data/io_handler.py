import logging
from pathlib import Path
import pandas as pd

from config.settings import (
    EXCEL_FILE,
    OUTPUT_CSV,
    OUTPUT_EXP_CSV,
    OUTPUT_EDU_CSV
)


def load_urls():
    if not Path(EXCEL_FILE).exists():
        logging.error(f"Input file not found: {EXCEL_FILE}")
        raise SystemExit(1)

    df = pd.read_excel(EXCEL_FILE)

    if "url" not in df.columns:
        logging.error("Excel must contain a column named 'url'")
        raise SystemExit(1)

    urls = df["url"].dropna().astype(str).tolist()

    if not urls:
        logging.error("No URLs found in the Excel file.")
        raise SystemExit(1)

    return urls


def save_profiles(profiles):
    df = pd.DataFrame(profiles)
    df.to_csv(OUTPUT_CSV, index=False, encoding="utf-8-sig")
    logging.info(f"Saved profiles CSV → {OUTPUT_CSV}")


def save_normalized(exp_rows, edu_rows):
    if exp_rows:
        pd.DataFrame(exp_rows).to_csv(OUTPUT_EXP_CSV, index=False, encoding="utf-8-sig")
        logging.info(f"Saved normalized experiences → {OUTPUT_EXP_CSV}")
    else:
        logging.info("No experiences found to normalize.")

    if edu_rows:
        pd.DataFrame(edu_rows).to_csv(OUTPUT_EDU_CSV, index=False, encoding="utf-8-sig")
        logging.info(f"Saved normalized education → {OUTPUT_EDU_CSV}")
    else:
        logging.info("No education found to normalize.")

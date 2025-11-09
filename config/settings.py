import logging
import os
from dotenv import load_dotenv

load_dotenv()

EXCEL_FILE = "profiles.xlsx"

LINKEDIN_EMAIL = os.getenv("LINKEDIN_EMAIL")
LINKEDIN_PASSWORD = os.getenv("LINKEDIN_PASSWORD")

OUTPUT_DIR = "output"
OUTPUT_CSV = f"{OUTPUT_DIR}/profiles.csv"
OUTPUT_EXP_CSV = f"{OUTPUT_DIR}/experiences_normalized.csv"
OUTPUT_EDU_CSV = f"{OUTPUT_DIR}/education_normalized.csv"

MAX_PROFILES = 20

# Browser configuration
USE_CHROME_PROFILE = True
CHROME_USER_DATA_DIR = os.getenv("CHROME_USER_DATA_DIR")
HEADLESS = False
MAX_WAIT = 12              # seconds for waiting page elements

MIN_DELAY = 3.0
MAX_DELAY = 7.0

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

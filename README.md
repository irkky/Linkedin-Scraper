# LinkedIn Profile Scraper

This project is a Python-based web scraper designed to extract data from LinkedIn profiles. It uses Selenium for browser automation and BeautifulSoup for HTML parsing to gather information such as name, headline, location, work experience, and education.

## Features

- **Bulk Scraping**: Reads a list of LinkedIn profile URLs from an Excel file (`profiles.xlsx`).
- **Data Extraction**: Scrapes key details from each profile:
  - Name, Headline, Location, and About section.
  - Detailed Work Experience and Education history.
- **Automated Login**: Automatically logs into a LinkedIn account to access profile data.
- **Data Normalization**: Processes and normalizes raw work experience and education history into a structured, row-based format.
- **CSV Output**: Saves the scraped data into multiple, easy-to-use CSV files.
- **Configurable & Resilient**:
  - Easily configure credentials and browser settings via a `.env` file.
  - Use an existing Chrome profile to potentially bypass repeated logins and CAPTCHAs.
  - Polite scraping with randomized delays to minimize the risk of being blocked.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/linkedin-scraper.git
    cd linkedin-scraper
    ```

2.  **Create and activate a virtual environment:**
    - On Windows:
      ```bash
      python -m venv venv
      venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      python3 -m venv venv
      source venv/bin/activate
      ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1.  **Create a `.env` file** in the root directory by copying the example:
    ```bash
    # You can create this file manually
    ```
    Then, add the following variables to the `.env` file:
    ```env
    LINKEDIN_EMAIL="your-linkedin-email@example.com"
    LINKEDIN_PASSWORD="your-linkedin-password"

    # Optional: To use an existing Chrome session and avoid login issues,
    # provide the path to your Chrome user data directory.
    # Find it at chrome://version > "Profile Path"
    # CHROME_USER_DATA_DIR="C:/Users/YourUser/AppData/Local/Google/Chrome/User Data"
    ```

2.  **Add Profile URLs**: Populate the `profiles.xlsx` file with the LinkedIn profile URLs you want to scrape. The URLs should be in the first column, one per row.

3.  **Customize Settings (Optional)**: Review and customize the settings in `config/settings.py` if needed. You can adjust:
    - `MAX_PROFILES`: The maximum number of profiles to process.
    - `HEADLESS`: Set to `True` to run the browser in the background.
    - `USE_CHROME_PROFILE`: Set to `True` if you provide `CHROME_USER_DATA_DIR` in your `.env`.

## Usage

Once configured, run the scraper from your terminal:
```bash
python main.py
```
The script will log its progress in the console and save the results in the `output` directory.

## Output File Descriptions

The scraper generates three CSV files in the `output` directory:

#### `1. profiles.csv`
This file contains the main information for each scraped profile.

| Column      | Description                                                              |
|-------------|--------------------------------------------------------------------------|
| `url`       | The original LinkedIn profile URL.                                       |
| `name`      | The full name of the person.                                             |
| `headline`  | The professional headline displayed below the name.                      |
| `location`  | The geographical location of the person.                                 |
| `about`     | The content of the "About" section.                                      |
| `experiences`| Raw, combined text of all work experiences, separated by `|||`.         |
| `education` | Raw, combined text of all education entries, separated by `|||`.         |

#### `2. experiences_normalized.csv`
This file contains a structured list of all work experiences from all scraped profiles.

| Column      | Description                               |
|-------------|-------------------------------------------|
| `profile_url`| The LinkedIn URL of the profile this experience belongs to. |
| `experience`| A single, distinct work experience entry. |

#### `3. education_normalized.csv`
This file contains a structured list of all education entries from all scraped profiles.

| Column      | Description                               |
|-------------|-------------------------------------------|
| `profile_url`| The LinkedIn URL of the profile this education entry belongs to. |
| `education` | A single, distinct education entry.       |

## Troubleshooting

- **Login Failures / CAPTCHA**: LinkedIn may require a CAPTCHA if you log in too frequently. To mitigate this:
  - Use an existing Chrome profile by setting `USE_CHROME_PROFILE = True` and providing your `CHROME_USER_DATA_DIR` in the `.env` file. This uses your existing login session.
  - If running in headless mode, try setting `HEADLESS = False` to solve the CAPTCHA manually in the browser window that opens.
- **Scraper is Blocked or Fails**: If the scraper fails to extract data, LinkedIn may have updated its website structure. The CSS selectors in `core/scraper.py` may need to be updated.
- **Empty Output Files**: Ensure that the profile URLs in `profiles.xlsx` are correct and that your LinkedIn account has access to view them. Check the console for any error messages.

## Disclaimer

This tool is intended for educational and research purposes only. Scraping data from websites may be against their Terms of Service. Users of this tool are responsible for ensuring they comply with all applicable laws and the terms of service of LinkedIn. The developers of this tool are not responsible for any misuse. Please use this scraper responsibly and ethically.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

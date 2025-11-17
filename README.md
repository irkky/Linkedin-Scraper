# 🔍 LinkedIn Profile Scraper

<div align="center">

![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Selenium](https://img.shields.io/badge/selenium-4.0+-orange.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

*A powerful Python-based web scraper for extracting comprehensive data from LinkedIn profiles*

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Output](#-output) • [Troubleshooting](#-troubleshooting)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [Output Structure](#-output-structure)
- [Project Architecture](#-project-architecture)
- [Troubleshooting](#-troubleshooting)
- [Best Practices](#-best-practices)
- [Disclaimer](#-disclaimer)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎯 Overview

The **LinkedIn Profile Scraper** is an automated tool that extracts valuable information from LinkedIn profiles at scale. Built with Selenium and BeautifulSoup, it navigates through LinkedIn profiles, extracts key information, and organizes the data into structured CSV files for easy analysis.

### What Can It Extract?

- ✅ **Personal Information**: Name, headline, location
- ✅ **About Section**: Complete profile summary
- ✅ **Work Experience**: Detailed employment history
- ✅ **Education**: Academic background and credentials
- ✅ **Normalized Data**: Structured, row-based format for analysis

---

## ✨ Features

### 🚀 Core Capabilities

| Feature | Description |
|---------|-------------|
| **Bulk Processing** | Scrape multiple profiles from an Excel file in one run |
| **Auto Login** | Automated LinkedIn authentication with credential management |
| **Smart Extraction** | Intelligent parsing of profile sections using multiple strategies |
| **Data Normalization** | Converts nested data into flat, analysis-ready CSV files |
| **Chrome Profile Support** | Use existing browser sessions to avoid repeated logins |
| **Rate Limiting** | Randomized delays to mimic human behavior |
| **Error Handling** | Robust exception handling with detailed logging |
| **Configurable** | Easy customization through `.env` and settings files |

### 🛡️ Built-in Protections

- **Polite Scraping**: Randomized delays between requests (3-7 seconds)
- **Anti-Detection**: Disabled automation flags and infobars
- **Session Reuse**: Optional Chrome profile usage to maintain login state
- **Timeout Management**: Configurable page load and element wait times

---

## 📦 Prerequisites

Before you begin, ensure you have:

- **Python 3.7+** installed on your system
- **Google Chrome** browser
- A **LinkedIn account** with valid credentials

---

## 🔧 Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/irkky/linkedin-scraper.git
cd linkedin-scraper
```

### Step 2: Create a Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Verify Installation

```bash
python main.py --help
```

---

## ⚙️ Configuration

### 1️⃣ Environment Variables

Create a `.env` file in the project root:

```env
# LinkedIn Credentials (Required)
LINKEDIN_EMAIL="your-email@example.com"
LINKEDIN_PASSWORD="your-secure-password"

# Chrome Profile Path (Optional but Recommended)
# Windows Example:
CHROME_USER_DATA_DIR="C:/Users/YourUsername/AppData/Local/Google/Chrome/User Data"

# macOS Example:
# CHROME_USER_DATA_DIR="/Users/YourUsername/Library/Application Support/Google/Chrome"

# Linux Example:
# CHROME_USER_DATA_DIR="/home/YourUsername/.config/google-chrome"
```

> 💡 **Finding Your Chrome Profile Path:**
> 1. Open Chrome
> 2. Navigate to `chrome://version`
> 3. Look for "Profile Path" and copy the directory up to "User Data"

### 2️⃣ Settings Configuration

Edit `config/settings.py` to customize behavior:

```python
# Maximum number of profiles to scrape
MAX_PROFILES = 20

# Run browser in background (headless mode)
HEADLESS = False

# Use existing Chrome profile (recommended)
USE_CHROME_PROFILE = True

# Maximum wait time for page elements (seconds)
MAX_WAIT = 12

# Delay range between requests (seconds)
MIN_DELAY = 3.0
MAX_DELAY = 7.0
```

### 3️⃣ Input File Setup

Create `profiles.xlsx` in the project root with a single column named `url`:

| url |
|-----|
| https://www.linkedin.com/in/example-profile-1/ |
| https://www.linkedin.com/in/example-profile-2/ |
| https://www.linkedin.com/in/example-profile-3/ |

---

## 🚀 Usage

### Basic Usage

```bash
python main.py
```

### Expected Output

```
2025-11-17 10:30:15 [INFO] Processing 20 profile URLs
2025-11-17 10:30:16 [INFO] Logging into LinkedIn...
2025-11-17 10:30:20 [INFO] Logged in successfully!
2025-11-17 10:30:21 [INFO] [1/20] Scraping: https://www.linkedin.com/in/example/
2025-11-17 10:30:28 [INFO] [2/20] Scraping: https://www.linkedin.com/in/another/
...
2025-11-17 10:45:30 [INFO] Saved profiles CSV → output/profiles.csv
2025-11-17 10:45:31 [INFO] Saved normalized experiences → output/experiences_normalized.csv
2025-11-17 10:45:31 [INFO] Saved normalized education → output/education_normalized.csv
```

---

## 📊 Output Structure

The scraper generates three CSV files in the `output/` directory:

### 1. `profiles.csv` - Main Profile Data

| Column | Description | Example |
|--------|-------------|---------|
| `url` | LinkedIn profile URL | https://linkedin.com/in/johndoe |
| `name` | Full name | John Doe |
| `headline` | Professional headline | Senior Software Engineer at TechCorp |
| `location` | Geographic location | San Francisco, California, United States |
| `about` | About section content | Passionate engineer with 10+ years... |
| `experiences` | Raw work history (separated by `\|\|\|`) | Software Engineer at Google \|\|\| Developer at Microsoft |
| `education` | Raw education data (separated by `\|\|\|`) | BS Computer Science, MIT \|\|\| MBA, Stanford |

### 2. `experiences_normalized.csv` - Flattened Work History

| Column | Description |
|--------|-------------|
| `url` | Profile URL |
| `name` | Person's name |
| `experience_text` | Single work experience entry |

**Example:**
```csv
url,name,experience_text
https://linkedin.com/in/johndoe,John Doe,"Senior Software Engineer at Google · Full-time · 2020 - Present · Mountain View, CA"
https://linkedin.com/in/johndoe,John Doe,"Software Developer at Microsoft · Full-time · 2018 - 2020 · Seattle, WA"
```

### 3. `education_normalized.csv` - Flattened Education History

| Column | Description |
|--------|-------------|
| `url` | Profile URL |
| `name` | Person's name |
| `education_text` | Single education entry |

**Example:**
```csv
url,name,education_text
https://linkedin.com/in/johndoe,John Doe,"Massachusetts Institute of Technology · Bachelor of Science - BS, Computer Science · 2014 - 2018"
https://linkedin.com/in/johndoe,John Doe,"Stanford University · Master of Business Administration - MBA · 2018 - 2020"
```

---

## 🏗️ Project Architecture

```
linkedin-scraper/
│
├── 📁 config/
│   └── settings.py          # Configuration and environment variables
│
├── 📁 core/
│   ├── driver_builder.py    # Selenium WebDriver setup
│   ├── login.py             # LinkedIn authentication logic
│   ├── scraper.py           # Profile extraction logic
│   └── utils.py             # Helper functions
│
├── 📁 data/
│   ├── io_handler.py        # File I/O operations
│   └── normalizer.py        # Data normalization functions
│
├── 📁 output/               # Generated CSV files (created at runtime)
│
├── .env                     # Environment variables (create this)
├── .gitignore              # Git ignore rules
├── LICENSE                 # MIT License
├── main.py                 # Entry point
├── profiles.xlsx           # Input file (create this)
├── README.md              # This file
└── requirements.txt       # Python dependencies
```

### Module Descriptions

| Module | Purpose |
|--------|---------|
| `driver_builder.py` | Configures and initializes Selenium Chrome driver with anti-detection measures |
| `login.py` | Handles LinkedIn authentication and session management |
| `scraper.py` | Core scraping logic with BeautifulSoup and Selenium selectors |
| `utils.py` | Utility functions for text extraction and directory management |
| `io_handler.py` | Manages reading Excel input and writing CSV output |
| `normalizer.py` | Transforms nested data into flat, analysis-ready format |

---

## 🔧 Troubleshooting

### Common Issues and Solutions

<details>
<summary><b>🔴 Login Failures / CAPTCHA Required</b></summary>

**Problem:** LinkedIn blocks login or requires CAPTCHA verification.

**Solutions:**
1. **Use Chrome Profile** (Recommended):
   ```python
   # In config/settings.py
   USE_CHROME_PROFILE = True
   ```
   Add `CHROME_USER_DATA_DIR` to your `.env` file

2. **Disable Headless Mode**:
   ```python
   HEADLESS = False
   ```
   Complete CAPTCHA manually in the browser window

3. **Wait Between Runs**: Avoid running the scraper too frequently from the same IP
</details>

<details>
<summary><b>🔴 Empty Output Files</b></summary>

**Problem:** CSV files are created but contain no data or only headers.

**Checks:**
- ✅ Verify URLs in `profiles.xlsx` are correct and accessible
- ✅ Ensure your LinkedIn account can view the profiles
- ✅ Check console logs for error messages
- ✅ Try increasing `MAX_WAIT` in settings
- ✅ Confirm you're logged in successfully
</details>

<details>
<summary><b>🔴 ChromeDriver Version Mismatch</b></summary>

**Problem:** Selenium can't find or launch ChromeDriver.

**Solution:**
```bash
pip install --upgrade webdriver-manager
```
The script automatically downloads the correct ChromeDriver version.
</details>

<details>
<summary><b>🔴 Selectors Not Working / Page Structure Changed</b></summary>

**Problem:** LinkedIn updated their HTML structure.

**Solution:**
Update CSS selectors in `core/scraper.py`. Example:
```python
# Old selector
data["headline"] = element_text_or_none(driver, By.CSS_SELECTOR, "div.text-body-medium")

# Try alternative selectors
data["headline"] = element_text_or_none(driver, By.CSS_SELECTOR, "div.new-headline-class")
```
</details>

<details>
<summary><b>🔴 Timeout Errors</b></summary>

**Problem:** Pages take too long to load.

**Solution:**
```python
# In config/settings.py
MAX_WAIT = 20  # Increase from 12 to 20 seconds
```
</details>

---

## 💡 Best Practices

### ✅ Do's

- ✨ **Start Small**: Test with 2-3 profiles before bulk scraping
- ✨ **Use Chrome Profile**: Reuse existing sessions to avoid login issues
- ✨ **Respect Rate Limits**: Don't decrease `MIN_DELAY` below 3 seconds
- ✨ **Monitor Logs**: Watch console output for warnings and errors
- ✨ **Backup Data**: Keep backups of scraped data
- ✨ **Update Regularly**: LinkedIn changes their layout frequently

### ❌ Don'ts

- ❌ **Don't Spam**: Avoid scraping thousands of profiles in one session
- ❌ **Don't Share Credentials**: Never commit `.env` to version control
- ❌ **Don't Ignore Errors**: Address warnings to prevent account restrictions
- ❌ **Don't Run 24/7**: Use reasonable intervals between scraping sessions
- ❌ **Don't Scrape Private Profiles**: Respect privacy settings

---

## ⚖️ Disclaimer

> **⚠️ IMPORTANT: READ CAREFULLY**

This tool is provided for **educational and research purposes only**. Web scraping may violate LinkedIn's Terms of Service. By using this tool, you acknowledge that:

1. **You are solely responsible** for ensuring compliance with:
   - LinkedIn's Terms of Service
   - Applicable data protection laws (GDPR, CCPA, etc.)
   - Copyright and intellectual property laws
   - Local regulations in your jurisdiction

2. **The developers are not liable** for:
   - Misuse of this tool
   - Account suspensions or bans
   - Legal consequences resulting from use
   - Data accuracy or integrity issues

3. **Ethical Usage**: You agree to:
   - Respect privacy and data protection laws
   - Use scraped data responsibly
   - Not use data for spam or harassment
   - Obtain proper consent when required

**Use this tool responsibly and at your own risk.**

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

### Ways to Contribute

- 🐛 **Report Bugs**: Open an issue with detailed reproduction steps
- 💡 **Suggest Features**: Share ideas for improvements
- 📝 **Improve Documentation**: Fix typos or add examples
- 🔧 **Submit Pull Requests**: Fix bugs or add new features

### Contribution Guidelines

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

### Code Standards

- Follow PEP 8 style guidelines
- Add comments for complex logic
- Update documentation for new features
- Test your changes before submitting

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License - Copyright (c) 2025 irkky
```

---

## 🙏 Acknowledgments

- **Selenium** - Browser automation framework
- **BeautifulSoup** - HTML parsing library
- **Pandas** - Data manipulation and analysis
- **webdriver-manager** - Automatic ChromeDriver management

---

## 📬 Support

- 📧 **Email**: Create an issue on GitHub
- 💬 **Discussions**: Use GitHub Discussions for questions
- 🐛 **Bug Reports**: Open an issue with the bug template
- ⭐ **Star this repo** if you find it useful!

---

<div align="center">

**Made with ❤️ by [irkky](https://github.com/irkky)**

⭐ Star this repo if it helped you! ⭐

[Back to Top](#-linkedin-profile-scraper)

</div>

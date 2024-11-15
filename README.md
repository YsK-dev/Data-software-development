
# Bundesliga Match Data Scraper

This project is just part of another project.Python-based web scraper designed to extract Bundesliga match data (seasons, match days, dates, teams, and results) from the official Bundesliga website. The scraped data is saved into a structured CSV file for further analysis.

---

## Features

- **Dynamic Season and Week Support**: Scrapes match data from the 2017-2024 Bundesliga seasons across all match weeks (1-34).  
- **Match Details Extraction**:
  - Date of the match
  - Home and away teams
  - Scores and results
- **CSV Export**: Saves the data into a CSV file for easy use in data analysis or visualization tools.

---

## Requirements

Before running the script, ensure you have the following installed:

- Python 3.8 or later
- Selenium (`pip install selenium`)
- Firefox browser
- GeckoDriver (WebDriver for Firefox, installed and added to the system PATH)

---

## Setup

1. **Install Selenium**:  
   ```bash
   pip install selenium

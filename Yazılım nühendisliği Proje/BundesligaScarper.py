#import 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time

# Set up WebDriver
options = webdriver.FirefoxOptions()# because of I use arch it was better option firefox
options.headless = True#no gui no trouble
driver = webdriver.Firefox(options=options)

# Define seasons and matchdays
years = range(2017, 2025)#why I started from 2017 because the website was showing results from 2017
match_days = range(1, 35)#and weeeks
# Initialize a list to store all match data
all_matches = []

def get_date_for_match(row):#the function 
    """"
    Find the date of a match from its closest preceding match-date-header element.
    This ensures that even if rows dont explicitly include the date,
    we can retrieve it from a shared date header.
    """
    try:
        # Check previous elements or container with date
        date_element = row.find_element(By.XPATH, 'preceding::match-date-header[1]')#ı felt a lot pain with xpath and css selector not always work properly
        return date_element.text.strip()
    except Exception as e:
        print(f"Date extraction failed: {e}")#I was always see this And I thought It wont work
        return "Unknown Date"# return a placeholder
#recursion structure
for year in years:
    next_year = year + 1#this for url url is like 2017-2018 for each year so in this way ı acsess the url
    for week in match_days:
        url = f'https://www.bundesliga.com/en/bundesliga/matchday/{year}-{next_year}/{week}'#the website
        driver.get(url)
        print(f"Scraping: {url}")

        try:
            # Wait for the main content
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'fixturescomponent'))#the componenet that holds matchs
            )
            match_rows = driver.find_elements(By.CSS_SELECTOR, '.matchRow')
            
            for row in match_rows:
                try:
                    date = get_date_for_match(row)
                    home_team = row.find_element(By.CSS_SELECTOR, 'match-team[side="home"] .name').text.strip()
                    away_team = row.find_element(By.CSS_SELECTOR, 'match-team[side="away"] .name').text.strip()
                    home_score = row.find_element(By.CSS_SELECTOR, 'score-bug .cell.home .score').text.strip()
                    away_score = row.find_element(By.CSS_SELECTOR, 'score-bug .cell.away .score').text.strip()
                    result = f"{home_score}-{away_score}"
                    
                    all_matches.append({
                        'season': f"{year}-{next_year}",
                        'match_day': week,
                        'date': date,
                        'home_team': home_team,
                        'away_team': away_team,
                        'result': result
                    })
                except Exception as e:
                    print(f"Failed to extract match: {e}")
        except Exception as e:
            print(f"Failed to load page or content: {e}")

        time.sleep(1)

driver.quit()

# Save to CSV
csv_file = 'bundesliga-full_data.csv'
csv_columns = ['season', 'match_day', 'date', 'home_team', 'away_team', 'result']# the way I save the data 

with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=csv_columns)
    writer.writeheader()
    writer.writerows(all_matches)

print(f"Fİnally Data saved to {csv_file}")

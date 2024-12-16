import pandas as pd
import requests
from bs4 import BeautifulSoup as soup
from functools import reduce
import time
import logging
import sys
from urllib.error import HTTPError

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_data_info():
    """
    Prompts user to select a league and season, returning the formatted URL, league name, and season.
    """
    leagues = {
        'Premier League': ('Premier-League', '9'),
        'La Liga': ('La-Liga', '12'),
        'Serie A': ('Serie-A', '11'),
        'Ligue 1': ('Ligue-1', '13'),
        'Bundesliga': ('Bundesliga', '20'),
        'Super Lig': ('Super-Lig', '26')
    }

    seasons = ['2017-2018', '2018-2019', '2019-2020', '2020-2021', '2021-2022']

    # Select league
    while True:
        league_input = input(f'Select League ({"/".join(leagues.keys())}): ')
        if league_input in leagues:
            league, league_id = leagues[league_input]
            break
        else:
            print('League not valid, try again.')

    # Select season
    while True:
        season = input(f'Select Season ({", ".join(seasons)}): ')
        if season in seasons:
            break
        else:
            print('Season not valid, try again.')

    url = f'https://fbref.com/en/comps/{league_id}/{season}/schedule/{season}-{league}-Scores-and-Fixtures'
    return url, league, season


def get_fixture_data(url, league, season):
    """
    Fetches fixture data for the specified league and season and saves it to a CSV file.
    """
    logging.info('Getting fixture data...')
    try:
        fixtures = pd.read_html(url)[0][['Wk', 'Day', 'Date', 'Time', 'Home', 'Away', 'xG', 'xG.1', 'Score']].dropna()
        fixtures['season'] = season
        fixtures['game_id'] = fixtures.index

        filename = f'{league.lower()}_{season.replace("-", "_")}_fixture_data.csv'
        fixtures.to_csv(filename, index=False)
        logging.info(f'Fixture data saved to {filename}')

    except Exception as e:
        logging.error(f'Error fetching fixture data: {e}')
        sys.exit(1)


def get_match_links(url, league):
    """
    Retrieves match links from the fixture page.
    """
    logging.info('Getting match links...')
    try:
        html = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        html.raise_for_status()
        links = soup(html.content, "html.parser").find_all('a')

        key_words_good = ['/en/matches/', league]
        match_links = ['https://fbref.com' + l.get('href') for l in links if all(x in l.get('href', '') for x in key_words_good)]
        return match_links

    except requests.RequestException as e:
        logging.error(f'Error fetching match links: {e}')
        sys.exit(1)


def fetch_player_data(match_links, league, season):
    """
    Fetches player data for each match and saves it to a CSV file.
    """
    logging.info('Getting player data...')
    player_data_df = pd.DataFrame([])

    for count, link in enumerate(match_links):
        try:
            tables = pd.read_html(link)
            logging.info(f'Processing match {count + 1}/{len(match_links)}')

            def get_team_data(start_index, is_home):
                data_frames = [tables[start_index], tables[start_index + 6]]
                df = reduce(lambda left, right: pd.merge(left, right, on=['Player', 'Nation', 'Age', 'Min'], how='outer'), data_frames).iloc[:-1]
                df['home'] = is_home
                df['game_id'] = count
                return df

            team1_data = get_team_data(3, 1)
            team2_data = get_team_data(10, 0)

            player_data_df = pd.concat([player_data_df, team1_data, team2_data])

            # Save after each match to avoid data loss
            filename = f'{league.lower()}_{season.replace("-", "_")}_player_data.csv'
            player_data_df.to_csv(filename, index=False)
            logging.info(f'Data saved to {filename}')

        except Exception as e:
            logging.error(f'Error processing {link}: {e}')

        # Sleep to avoid IP blocking
        time.sleep(3)


def main():
    url, league, season = get_data_info()
    get_fixture_data(url, league, season)
    match_links = get_match_links(url, league)
    fetch_player_data(match_links, league, season)

    # Ask if user wants to collect more data
    while True:
        answer = input('Do you want to collect more data? (yes/no): ').strip().lower()
        if answer == 'yes':
            main()
        elif answer == 'no':
            logging.info('Data collection complete. Exiting program.')
            sys.exit(0)
        else:
            print('Invalid answer. Please enter yes or no.')


if __name__ == '__main__':
    try:
        main()
    except HTTPError:
        logging.error('The website refused access. Try again later.')
        time.sleep(5)
    except KeyboardInterrupt:
        logging.info('Process interrupted by user.')
        sys.exit(0)

# DATA-440-Final-Project: NBA GameDay

### How To Run NBA GameDay:

1) Download zip file and navigate to the 'DATA-440-Final-Project' folder
2) Run:
  > pipenv install --ignore-pipfile
4) Run:
  > pipenv shell
5) Run:
  > streamlit run VI_execute_app.py
---

My initial premise was to predict the winner of NBA games using Machine Learning. I still will pursue this project on my own accord, but due to the time remaining in the semester, I’m pivoting to a new project: NBA GameDay

NBA GameDay is a Streamlit website that displays a dashboard of team statistics for the 2023-2024 NBA games on the current day. Users can look at a variety of statistics for the given teams playing each other, from basic statistics like Points Per Game, to more advanced statistics like True Shooting%, along with information on the team’s head-to-head history against each other. This platform allows anyone from the casual to the die-hard basketball fan to have readily-available information about their favorite games before they start, whether for their own entertainment or maybe before (responsibly) placing a wager.

This is not a finished product yet, as I some of the tasks I need to accomplish include:
1. Scrape Data for current 2023-2024 season
2. Finish adding the head-to-head, record features
3. Further Design Streamlit Page
4. Converting notebooks to .py files and modularizing all coe

However, the current code (11/30) for peer review gives an example of what the dashboard will contain. Specifically, the Streamlit page  displays a couple of statistics for a random date, just to show what it would look like with numerous games for a day.

## How to Use: 
1. Download Repository
2. Execute V_dashboard.py (streamlit run V_dashboard.py)

## Components:
Data: 
- nba_games.csv and nba_games_2023.csv:
  - first file: 2016-2022 NBA Box Score data, downloaded from GitHub repository (see note below)
  - second file: 2023 NBA Box Score data, outputted from I_data_scraping file
- Contains the scraped data for 2016-2022 and 2023 season
- Cleaned_nba_data - csv file that contains dataset after cleaning from notebook III (III_preprocessing.ipynb)
  - I.e. Dataset used for feature engineering 

Notebooks:
- I_data_scraping: code to scrape box score statistics from Basketball Reference
  - See Note about code below
- II_EDA: Exploratory Data Analysis
- III_preprocessing: Notebook that takes scraped data, preprocesses it, and writes into cleaned_nba_data.csv
- IV_feature_engineering.py: Functions that creates new features from the cleaned, preprocessed data
  - Why: Since the box score data is collected post-game, we want the ability to have data pre-game, since the premise is to produce statistics for games that haven't happened yet
- V_dashboard.py: Python file that creates Streamlit app with dashboard
           
Note About Web Scraping:
- Historical data is retrieved from GitHub, which is a csv file of NBA Box Score data from 2016-2022, originally scraped from Basketball Reference Seasons.
- I_data_scraping contains functions that I modified and adapted from the get_data and parse_data files from the same repository. This was done due to my inexperience with scraping and to keep uniformity with 2016-2022 dataset I downloaded from same repository       
  - Link: https://github.com/dataquestio/project-walkthroughs/blob/master/nba_games/README.md
    


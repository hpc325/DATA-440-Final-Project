# DATA-440-Final-Project: NBA GameDay


My initial premise was to predict the winner of NBA games using Machine Learning. I still will pursue this project on my own accord, but for the scope of this semester, I’m pivoted to a new project: NBA GameDay

NBA GameDay is a Streamlit website that displays a dashboard of team statistics for the final regular season NBA games of the 2023 NBA season. The user can choose the specific date they want to look at, and then they will see the given games for that day. Users can view at a variety of statistics for the given teams playing each other, from basic statistics like Points Per Game, to more advanced statistics like True Shooting%. If you're not truly versed with basketball, you can open up the legend on the side, which gives the description of each statistic's acronym.

Typically, many websites have plethora of NBA data. However, when you want to view data on specific games, you typically have to navigate through a couple of links to view that given matchup. The premise of this project was for the user to have an easy-to-access dashboard, where they can navigate to different games and statistics all on the same page. As a result, this platform allows anyone from the casual to the die-hard basketball fan to have readily available information about their favorite games before they start, whether for their own entertainment or before (legally and responsibly) placing a wager. 

### How To Run NBA GameDay:

1) Download zip file and navigate to the 'DATA-440-Final-Project' folder
2) Run:
  > pipenv install --ignore-pipfile
3) Run:
  > pipenv shell
4) Run:
  > streamlit run VI_execute_app.py


### Further Breakdown of Repositories and Files:
data: 
- Contains the scraped data for 2016-2022 and 2023 season
- **nba_games.csv and nba_games_2023.csv**:
  - first file: 2016-2022 NBA Box Score data, downloaded from GitHub repository (see note below)
  - second file: 2023 NBA Box Score data, outputted from I_data_scraping file
-**cleaned_nba_data.csv** - csv file that contains dataset after cleaning from notebook II (II_preprocessing.ipynb)
  - I.e. Dataset used for feature engineering 

data_notebooks:
- **I_data_scraping**: code to scrape box score statistics from Basketball Reference
  - *See Note about code below*
- **II_preprocessing**: Notebook that takes scraped data, preprocesses it, and writes into cleaned_nba_data.csv
- These notebooks are already executed, and since the Streamlit website is based on a fixed csv file (cleaned_nba_data.csv), these files aren't essential to executing streamlit file
  - The necessary files for Streamlit are in the src_files directory

src_files:
- **III_feature_engineering.py**: Functions that creates new features from the cleaned, preprocessed data
  - Why: Since the box score data is collected post-game, we want the ability to have data pre-game, since the premise is to produce statistics for games that haven't happened yet
  - Functionality:
    - Compute Averages and Rolling Averages (i.e. averages for a given period of games)
    - Separate Basic vs Advanced Statistics
- **IV_Streamlit_Prep.py**: Functions that convert features from file III and transforms them into readable format for Streamlit
  - Produces dataframe that shows statistics for each game in a vertical manner; the first and third columns are the Home and Away Team's respective statistic values, and the middle column contains the name of the stats. 
    - This allows viewer to easily compare statistic values between the two teams, rather than just giving a dataframe of statistics for all games on a given day (very clumpy!)
- **V_dashboard.py**: Python file that creates Streamlit app with dashboard
- Contains all the .py files necessary to feature engineering, data-styling prep for Streamlit, and Streamlit building functins

**VI_execute_app.py**: Python file that executes and runs the Streamlit website created in V_dashboard.py file
           
Note About Web Scraping:
- Historical data is retrieved from GitHub, which is a csv file of NBA Box Score data from 2016-2022, originally scraped from Basketball Reference Seasons.
- I_data_scraping contains functions that I modified and adapted from the get_data and parse_data files from the same repository. This was done due to my inexperience with scraping and to keep uniformity with 2016-2022 dataset I downloaded from same repository       
  - Link: https://github.com/dataquestio/project-walkthroughs/blob/master/nba_games/README.md

### Future Plans:
As I mentioned earlier, I want to continue working on predicting the outcome of NBA games using Machine Learning. I initially could not improve the accuracy substantially enough within this time scope, but what's encouraging is that the pivot to this statistics dashboard actually *helped* with predictive modeling. The dashboard is really centered around feature engineering, and as I was working on pivoting my project, I learned that I was creating the averages/rolling averages incorrectly for the opposing team. Later in the project, I went back to my modeling notebooks, applied the new feature functions, and immediately there was a boost in accuracy with all models!

I will definitely continue pursuing that project, but with respect to both NBA GameDay and the predictive modeling, they both come down to web scraping. I need to scrape not only the 2023-2024 NBA season data, but also create scripts that automates scraping the data after the most recent set of games and scrape the upcoming matchups for the next day. This will also involve backfilling the upcoming games with its resulting post-game data. Eventually, as you probably are wondering, I need to make a database to contain all of this data, rather than using a singular csv file. 

Additionally, for both the dashboard and the predictive modeling, I want to include additional features, including the respective teams' record, recent trends (i.e. how many games have they won/lost in the last 5 games), and their history against each other (ex: what's the Celtics record against the 76ers for the last 2 seasons?). These features will not only be useful for the user of NBA GameDay, but also in developing a ML model to predict the outcome of NBA games.
    


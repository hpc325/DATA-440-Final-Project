import pandas as pd
from src_files.III_feature_engineering import execute_feature_engineering

def execute_streamlit_data(clean_data,date,num_games,return_averages=False,return_rolling_averages=False,
                           return_basic=False,return_advanced=False):
    '''
        Pipeline to produce all the necessary data needed to show either averages or rolling averages data on streamlit

        Return dictionary, where each key's values is the dataframe of the matchup between two individual teams.
    '''
    
    if return_averages: # Return averages dataframe for all teams for given date
        averages = execute_feature_engineering(clean_data,averages=True)
        averages_date = clean_data_for_streamlit(averages,date) # Subset both averages and rolling averages for the given data
        home_df = subset_home_and_away_teams(averages_date) # Separate home and away teams dataframes
        away_df = subset_home_and_away_teams(averages_date,return_away=True)
        
        if return_basic: # If we want averages of basic stats
            final_home_df = subset_basic_and_advanced_stats(home_df) # Home and away teams' basic stats
            final_away_df = subset_basic_and_advanced_stats(away_df) 
        elif return_advanced: # Advanced averages 
            final_home_df = subset_basic_and_advanced_stats(home_df,advanced=True) # Home and away a
            final_away_df = subset_basic_and_advanced_stats(away_df,advanced=True) 
        
        
    elif return_rolling_averages: # Return rolling averages dataframe for all teams for given date
        rolling_averages = execute_feature_engineering(clean_data,num_games,rolling_averages=True)  # First calculate averages and rolling averages
        rolling_date = clean_data_for_streamlit(rolling_averages,date)
        home_df = subset_home_and_away_teams(rolling_date)
        away_df = subset_home_and_away_teams(rolling_date,return_away=True)
        
        if return_basic: # Basic Averages
            final_home_df = subset_basic_and_advanced_stats(home_df) # Home and away teams' basic stats
            final_away_df = subset_basic_and_advanced_stats(away_df) 
        elif return_advanced: # Advanced averages 
            final_home_df = subset_basic_and_advanced_stats(home_df,advanced=True) # Home and away a
            final_away_df = subset_basic_and_advanced_stats(away_df,advanced=True) 
       

    num_games = len(get_matchups(clean_data,date)) # Number of games played on this date
    statistic_matchups = {} # Dictionaries that keep the statistics between the two teams for each matchup; since we need to visually change how to show stats on Streamlit
    for i in range(num_games): # or rolling_averages; it will be the same
        statistic_matchups[i] = show_one_matchup(final_home_df,final_away_df,i)# i represents game id
        
    return statistic_matchups

def clean_data_for_streamlit(data,date):
    '''
        Return a dataframe cleaned up visually for Streamlit app
    '''
    
    new_df = data[data['date'] == date] # Subset date
    new_df = new_df[new_df['home'] == 1].reset_index(drop=True) # Keep home records
    new_df = new_df.drop(['season','date','home','target','game_id','won'],axis=1) # eventually drop season and date
    
    new_df = new_df.rename({'team':'Home Team','team_opp':'Away Team'},axis=1)
    
    ### Formatting
    # Multiply percentage columns by 100
    percentage_cols = ['fg%','fg%_opp','3p%','3p%_opp','ft%',
                       'ft%_opp','ts%','ts%_opp','efg%','efg%_opp']
    all_numeric_cols = new_df.columns[2:]
    remaining_cols = [c for c in all_numeric_cols if c not in percentage_cols]
    for c in percentage_cols: 
        new_df[c] *= 100
    for c in remaining_cols: # For columsn with more than 1 decimal point, round to 1
        new_df[c] = new_df[c].round(1)
    return new_df

def subset_home_and_away_teams(data,return_away=False):
    '''
        Return the home or away team's statistics for the given data
    '''
    away_cols = ['Away Team'] + [c for c in data.columns if '_opp' in c] 
    home_cols = [c for c in data.columns if '_opp' not in c]
    home_cols.remove('Away Team')
    #home_cols.remove('date')
    
    if return_away: # Return the away team's subset
        away_teams = data[away_cols] 
        away_teams.columns = [c.replace('_opp','') for c in away_teams.columns] # Remove _opp from away_stats to standardize col names
        return away_teams
    else: # Return the home team's subset
        return data[home_cols]

def subset_basic_and_advanced_stats(data,advanced=False):
    '''
        Return the basic or advanced statistics for the given dataframe
    '''
    team_name = data.iloc[:,0].name # Keep first three columns of either dataframe, which is the team name, season, and date
    all_stats = ['pts','fg', 'fga', 'fg%', '3p', '3pa', '3p%', 'ft', 'fta', 'ft%','orb', 'drb', 'trb', 
             'ast', 'stl', 'blk', 'tov', 'pf', 'ts%','efg%', '3par', 'ftr', 'orb%', 'drb%', 'trb%', 
             'ast%', 'stl%', 'blk%','tov%', 'ortg', 'drtg']
    if advanced: # Return advanced statistics
        return data[[team_name] + all_stats[18:]]
    else: # Return basic statistics
        return data[[team_name] + all_stats[:18]]

def show_one_matchup(home_df,away_df,game_id):
    '''
        Show the individual matchup selected in vertical manner.
        
        game_id = row index associated with the matchup; selected by user
        averages = True if user wants just averages
        rolling_averages= True if user wants rolling averages
    '''
    
    home_team = home_df.iloc[game_id,:]
    away_team = away_df.iloc[game_id,:]
    
    home_team = home_team.rename({'Home Team':'Team'})
    away_team = away_team.rename({'Away Team':'Team'})
    matchup = pd.DataFrame(data=[home_team,away_team]).T

    stat_column = list(matchup.index) # Create middle column separating home and away team with the statistic
    stat_column = [c.upper() for c in stat_column]
    matchup.insert(1,'State',stat_column)
    matchup = matchup.reset_index(drop=True)
    
    matchup.columns = matchup.iloc[0,:]
    matchup = matchup.iloc[1:,:]
    return matchup

def get_matchups(data,date):
    '''
        Return a dictionary with the two teams competing against each other as the key, and the row index as the value;
        value will be used for indexing the statistics that'll be shown
        
        data = cleaned nba box score data obtained from preprocessing
    '''
    
    subset = data[data['date'] == date]
    subset = subset[subset['home'] == 1].reset_index(drop=True)
    subset = subset[['team','team_opp','season','date']]

    game_info = {}

    for i in range(len(subset)):
        row = subset.iloc[i,:]
        game_info[f"{row['team']} vs. {row['team_opp']}"] = i
    return game_info
    
        

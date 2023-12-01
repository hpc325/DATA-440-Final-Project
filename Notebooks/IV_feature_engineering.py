import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def create_model_variables(data):
    model_variables = list(data.columns)
    meta_vars =['Home Team','Away Team','season','date','won','target','index_opp']
    model_variables = [col for col in model_variables if col not in meta_vars]
    
    return model_variables

def create_averages(data, model_variables, num_games=3, rolling_average=False):
    '''
    Return dataframe with averages of each model variable leading up to each game. 
    
    data = nba_clean_data (cleaned nba box score data)
    model_variables = numeric columns to compute averages for
    num_games = 3; default value if we want to return the rolling average, rather than the average for the season
    rolling_average=False; if set to True, compute rolling average
    '''
    data = data.sort_values(['Home Team','season','date']).reset_index(drop=True) # Need to order by team, season, and date
    meta_vars = ['Home Team','Away Team','season','date']
    meta_vars_df = data[meta_vars].reset_index(drop=True)
    
    averages_df = pd.DataFrame()
    for stat in model_variables:
        if rolling_average: # If rolling_average is set to True, compute rolling average for specified window
            rolling_avg_stat = data.groupby(['Home Team','season'])[stat].rolling(window=num_games).mean().round(1).reset_index(drop=True)
            averages_df.loc[:,stat] = rolling_avg_stat
        else: # If it's just computing average for the given season
            average_stat = data.groupby(['Home Team','season'])[stat].expanding(1).mean().round(1).reset_index(drop=True)
            averages_df.loc[:,stat] = average_stat
        
    final_df = pd.concat([meta_vars_df,averages_df],axis=1)
    final_df = final_df.sort_values(['season','date']).reset_index(drop=True)
    return final_df
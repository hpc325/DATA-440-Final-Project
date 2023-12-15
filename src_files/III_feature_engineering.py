import pandas as pd


def separate_team_and_opponent(data):
    '''
    Return two new dataframes by splitting nba data by keeping or removing '_opp'
    
    '''
    meta_vars = ['season','date','game_id']
    vars_to_separate = [v for v in data.columns if v not in meta_vars]
    
    teams_vars = [var for var in vars_to_separate if '_opp' not in var] # Grab team variables (i.e. w/o _opp)
    opp_vars = [var for var in vars_to_separate if 'opp' in var]
    
    all_team_vars = meta_vars[0:3] + teams_vars 
    all_opp_vars = meta_vars[0:3] + opp_vars 
    
    team_df = data[all_team_vars].reset_index(drop=True)
    opp_df = data[all_opp_vars].reset_index(drop=True)
    
    return team_df,opp_df

def create_team_averages(data,num_games=3,rolling_average=False):
    
    data = data.sort_values(['team','season','date']).reset_index(drop=True) # Need to order by team, season, and date
    meta_vars = ['team','season','date','home','won','target','game_id']
    meta_vars_df = data[meta_vars].reset_index(drop=True)
    
    cols_compute = [var for var in data.columns if var not in meta_vars]
    
    averages_df = pd.DataFrame()
    for stat in cols_compute:
        if rolling_average: # If rolling_average is set to True, compute rolling average for specified window
            rolling_avg_stat = data.groupby(['team','season'])[stat].rolling(window=num_games).mean().round(3).reset_index(drop=True)
            averages_df.loc[:,stat] = rolling_avg_stat
        else: # If it's just computing average for the given season
            average_stat = data.groupby(['team','season'])[stat].expanding(1).mean().round(3).reset_index(drop=True)
            averages_df.loc[:,stat] = average_stat
        
    final_df = pd.concat([meta_vars_df,averages_df],axis=1)
    final_df = final_df.sort_values(['game_id','season','date']).reset_index(drop=True)
    return final_df

def create_opp_averages(data,num_games=3,rolling_average=False):
    
    data = data.sort_values(['team_opp','season','date']).reset_index(drop=True) # Need to order by team, season, and date
    meta_vars = ['team_opp','season','date','game_id'] # Less meta vars for opponent averages
    meta_vars_df = data[meta_vars].reset_index(drop=True)
    
    cols_compute = [var for var in data.columns if var not in meta_vars]
    
    averages_df = pd.DataFrame()
    for stat in cols_compute:
        if rolling_average: # If rolling_average is set to True, compute rolling average for specified window
            rolling_avg_stat = data.groupby(['team_opp','season'])[stat].rolling(window=num_games).mean().round(3).reset_index(drop=True)
            averages_df.loc[:,stat] = rolling_avg_stat
        else: # If it's just computing average for the given season
            average_stat = data.groupby(['team_opp','season'])[stat].expanding(1).mean().round(3).reset_index(drop=True)
            averages_df.loc[:,stat] = average_stat
        
    final_df = pd.concat([meta_vars_df,averages_df],axis=1)
    final_df = final_df.sort_values(['game_id','season','date']).reset_index(drop=True)
    return final_df
    
def concat_calculations(team_calc_df,opp_calc_df):
    '''
        Return dataframe with the teams' and opponents' statistics concatenated again
    '''
    combined_df = pd.concat([team_calc_df,opp_calc_df],axis=1) # Since both dataframes are ordered by game id, they can be concatenated
    combined_df = combined_df.loc[:,~combined_df.columns.duplicated()]
    
    col_to_move = combined_df.pop('team_opp') # Move opponent team name to front of dataframe
    combined_df.insert(1,'team_opp',col_to_move)
    
    return combined_df


def execute_feature_engineering(data,num_games=3,averages=False,rolling_averages=False):
    '''
        Execute feature engineering for calculating either general averages or rolling averages; 
        
        num_games = number of games wanted to calculate rolling average (if set to True)
        Note: averages or rolling_averages have to equal True
    '''
    team_df, opp_df = separate_team_and_opponent(data)
    
    if averages:
        team_df = create_team_averages(team_df)
        opp_df = create_opp_averages(opp_df)
    if rolling_averages:
        team_df = create_team_averages(team_df,num_games,True)
        opp_df = create_opp_averages(opp_df,num_games,True)
    
    final_df = concat_calculations(team_df,opp_df) 
    return final_df
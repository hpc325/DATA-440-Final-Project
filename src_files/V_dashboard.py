import os
import pandas as pd
import streamlit as st
from src_files.IV_Streamlit_Prep import execute_streamlit_data, get_matchups

def main():

    cur_dir = os.path.dirname(os.path.abspath(__file__)) # Get the directory of the current script
    data_dir = os.path.join(cur_dir, '..', 'data') # Navigate up one directory to get data directory
    data_path = os.path.join(data_dir, 'cleaned_nba_data.csv')
    nba_clean_data = pd.read_csv(data_path)
    given_dates = ['2023-04-09','2023-04-08','2023-04-07','2023-04-06','2023-04-05'] # Final 5 dates of the 2023 NBA regular season
   

    basic_stats_glossary = {'PTS':'Points','FG':'Field Goals','FGA':'Field Goal Attempts','FG%':'Field Goal Percentage','3P':'3-Point Field Goals',
    '3PA': '3-Point Field Goal Attempts','3P%':'3-Point Field Goal Percentage','FT':'Free Throws','FTA':'Free Throw Attempts',
    'FT%':'Free Throw Percentage','ORB':'Offensive Rebounds','DRB':'Defensive Rebounds','TRB':'Total Rebounds','AST':'Assists','STL':'Steals',
    'BLK':'Blocks','TOV':'Turnovers','PF':'Personal Fouls'}

    advanced_stats_glossary = {'TS%':'True Shooting Percentage','eFG%':'Effective Field Goal Percentage','3PAr':'3-Point Attempt Rate',
    'FTr':'Free Throw Attempt Rate','ORB%':'Offensive Rebound Percentage','DRB%':'Defensive Rebound Percentage','TRB%':'Total Rebound Percentage',
    'AST%':'Assist Percentage','STL%':'Steal Percentage','BLK%':'Block Percentage','TOV%':'Turnover Percentage',
    'ORTG':'Offensive Rating','DRTG':'Defensive Rating'}

    st.title(f":orange[NBA GameDay] :basketball") # Create title

    col1,col2,col3 = st.columns([1.5,1.5,1])

    with col1:
        date_option = st.selectbox('Select Date:', given_dates)
        all_matchups = get_matchups(nba_clean_data,date_option)
        matchup_option = st.radio('Select Matchup (Home vs. Away):',(all_matchups.keys()))
        stat_option = st.radio('Select Type of Statistics:', ('Basic','Advanced'))
        average_option = st.radio('Select Type of Average:', ('Averages', 'Rolling Averages'))
        window_option = st.radio('Sample Size (Rolling Averages):',(2,3,4,5))


    with col2:
        if stat_option == 'Basic':
            if average_option == 'Averages': # Basic Averages
                basic_averages = execute_streamlit_data(nba_clean_data,date_option,None,return_averages=True,return_basic=True)
                matchup = basic_averages[all_matchups[matchup_option]]
                st.write(f"Head-to-Head {stat_option} {average_option}")
                st.dataframe(matchup,hide_index=True,width=200,height=665) # Highlight better value for each stat
            else: # Basic Rolling Averages 
                basic_rolling = execute_streamlit_data(nba_clean_data,date_option,window_option,return_rolling_averages=True,return_basic=True)
                matchup = basic_rolling[all_matchups[matchup_option]]
                st.write(f"Head-to-Head {stat_option} {average_option}")
                st.dataframe(matchup,hide_index=True,width=200,height=665)
        elif stat_option == 'Advanced':
            if average_option == 'Averages': # Advanced Averages
                advanced_averages = execute_streamlit_data(nba_clean_data,date_option,None,return_averages=True,return_advanced=True)
                matchup = advanced_averages[all_matchups[matchup_option]]
                st.write(f"Head-to-Head {stat_option} {average_option}")
                st.dataframe(matchup,hide_index=True,width=200,height=490) # Highlight better value for each stat
            else: # Advanced Rolling Averages 
                advanced_rolling = execute_streamlit_data(nba_clean_data,date_option,window_option,return_rolling_averages=True,return_advanced=True)
                matchup = advanced_rolling[all_matchups[matchup_option]]
                st.write(f"Head-to-Head {stat_option} {average_option}")
                st.dataframe(matchup,hide_index=True,width=200,height=490)

    with col3:
        glossary_option = st.toggle('Show Legend')
        if glossary_option:
            if average_option == 'Averages':
                for stat,full_stat_name in basic_stats_glossary.items():
                    st.write(f"{stat} = {full_stat_name}")
            else:
                for stat,full_stat_name in advanced_stats_glossary.items():
                    st.write(f"{stat} = {full_stat_name}")

#if __name__ == '__main__':
   # main()


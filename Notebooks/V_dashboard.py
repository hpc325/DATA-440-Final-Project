import pandas as pd
import streamlit as st
import IV_feature_engineering as IV


st.title('NBA GameDay: Statistics Dashboard') # Create title

@st.cache_data
def load_data():
    nba_clean_data = pd.read_csv('../data/cleaned_nba_data.csv') # get most recent data
    model_variables = IV.create_model_variables(nba_clean_data) # Establish model variables
    nba_averages_df = IV.create_averages(nba_clean_data,model_variables)
    nba_rolling_df = IV.create_averages(nba_clean_data,model_variables,3,True)

    return nba_averages_df, nba_rolling_df

def display_data(data, given_date):
    data = data[data['date'] == given_date]
    dashboard_vars = ['Home Team','Away Team','pts','pts_opp','trb','trb_opp','fg%','fg%_opp'] # Just show basic stats for now; hardcoded for now
    df = data[dashboard_vars].reset_index(drop=True)
    return df



averages_df, rolling_df = load_data() # Load in both dataframes

most_recent_date = '2023-03-26'

data_option = st.radio('Select Option', ('Averages', 'Rolling Averages'))

if data_option == 'Averages':
    streamlit_df = display_data(averages_df,most_recent_date)
    st.subheader(f'{most_recent_date} {data_option}')
    st.write(streamlit_df)
else:
    streamlit_df = display_data(rolling_df,most_recent_date)
    st.subheader(f'{most_recent_date} {data_option}')
    st.write(streamlit_df)

# DATA-440-Final-Project: NBA Prediction Algorithm using Machine Learning

Predicting the winner of an NBA game isn't just a hunch. The ability to accurately predict the outcome of NBA matchups affects a wide-variety of stakeholders,
from the casual fans betting with their buddies, to the die-hards looking for a solid Moneyline pick on DraftKings, to even NBA scouts who are tasked with researching
their respective opposing team on a Tuesday night. 

This project aims to integrate Machine Learning techniques with a variety of basketball statistics to forecast the results of an NBA game. The model will predict the winner of each game (i.e. which team wins), along with the confidence level of the prediction (i.e probability of the winner). 

The end-product will be deploying the model via Streamlit, where this UI will display current NBA games and the model's subsequent predictions for each game. 
           
### Key Features:
- Historical data is retrieved from GitHub, which is NBA Box Score data from 2016-2022, originally scraped from Basketball Reference Seasons
- NBA Box Score Data from 2022-2023 season will serve as testing data, which will be scraped from Basketball Reference
- EDA, Preprocessing, and Feature Engineering will be performed before developing most effective model; trained on historical data (2016-2022).
- Test model on 2022-2023 NBA data, deploy model on 2023-2024 NBA games
- Create pipelines that scrapes most recent NBA games everyday and retrain model when needed, so that we can see how the model performs throughout season


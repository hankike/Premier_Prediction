import pandas as pd
import numpy as np

url = 'https://raw.githubusercontent.com/hankike/Premier_Prediction/refs/heads/main/data/premier_data_2019-2026.csv'

df_premier = pd.read_csv(url)

teams = sorted(set(df_premier["HomeTeam"]) | set(df_premier["AwayTeam"]))

records = []

for team in teams:
    home_games = df_premier[df_premier["HomeTeam"] == team]

    home_wins = (home_games["FTR"] == "H").sum()
    home_losses = (home_games["FTR"] == "A").sum()
    home_draws = (home_games["FTR"] == "D").sum()

    away_games = df_premier[df_premier["AwayTeam"] == team]

    away_wins = (away_games["FTR"] == "A").sum()
    away_losses = (away_games["FTR"] == "H").sum()
    away_draws = (away_games["FTR"] == "D").sum()

    records.append({
        "Team": team,
        "Wins": home_wins + away_wins,
        "Losses": home_losses + away_losses,
        "Draws": home_draws + away_draws,
        "Games": home_wins + away_wins + home_losses + away_losses + home_draws + away_draws
    })

results = pd.DataFrame(records)

results = results.sort_values("Games", ascending=False)

results

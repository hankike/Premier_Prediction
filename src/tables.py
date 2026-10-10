import pandas as pd

# First we create a records table


def create_results_table(url):
    df_premier = pd.read_csv(url)

    teams = sorted(
        set(df_premier["HomeTeam"]) |
        set(df_premier["AwayTeam"])
    )

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
            "Games": (
                home_wins + away_wins
                + home_losses + away_losses
                + home_draws + away_draws
            )
        })

    results = pd.DataFrame(records)

    return results.sort_values("Games", ascending=False)


# Next we create a win percentage table
def create_standings_table(url):
    df_premier = pd.read_csv(url)

    teams = sorted(
        set(df_premier["HomeTeam"]) |
        set(df_premier["AwayTeam"])
    )

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
            "Home Games": home_wins + home_losses + home_draws,
            "Home Win Percentage": (home_wins / (home_wins + home_draws + home_losses)).round(3),
            "Home Point Percentage": ((home_wins + home_draws) / (home_wins + home_draws + home_losses)).round(3),
            "Road Games": away_wins + away_losses + away_draws,
            "Road Win Percentage": (away_wins / (away_wins + away_draws + away_losses)).round(3),
            "Road Point Percentage": ((away_wins + away_draws) / (away_wins + away_draws + away_losses)).round(3)
        })

    standings = pd.DataFrame(records)

    return standings.sort_values("Home Win Percentage", ascending=False)

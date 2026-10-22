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


# Create a shots table
def create_shots_table(url):
    df_premier = pd.read_csv(url)

    teams = sorted(
        set(df_premier["HomeTeam"]) |
        set(df_premier["AwayTeam"])
    )

    records = []

    for team in teams:
        home_games = df_premier[df_premier["HomeTeam"] == team]

        home_goals_for = home_games["FTHG"].sum()
        home_shots_for = home_games["HS"].sum()

        away_games = df_premier[df_premier["AwayTeam"] == team]

        away_goals_for = away_games["FTAG"].sum()
        away_shots_for = away_games["AS"].sum()

        records.append({
            "Team": team,
            "Games": len(home_games) + len(away_games),
            "Shots Home": home_shots_for,
            "Goals Home": home_goals_for,
            "Home Shots per Goal": home_shots_for / home_goals_for if home_goals_for > 0 else 0,
            "Home Shots per Game": home_shots_for / (len(home_games) if len(home_games) > 0 else 1),
            "Shots Away": away_shots_for,
            "Goals Away": away_goals_for,
            "Away Shots per Goal": away_shots_for / away_goals_for if away_goals_for > 0 else 0,
            "Away Shots per Game": away_shots_for / (len(away_games) if len(away_games) > 0 else 1)
        })

    shots = pd.DataFrame(records)

    shots["Home Shots per Goal"] = shots["Home Shots per Goal"].round(2)
    shots["Home Shots per Game"] = shots["Home Shots per Game"].round(2)
    shots["Away Shots per Goal"] = shots["Away Shots per Goal"].round(2)
    shots["Away Shots per Game"] = shots["Away Shots per Game"].round(2)

    return shots


# Create shots against table
def create_shots_against_table(url):
    df_premier = pd.read_csv(url)

    teams = sorted(
        set(df_premier["HomeTeam"]) |
        set(df_premier["AwayTeam"])
    )

    records = []

    for team in teams:
        home_games = df_premier[df_premier["HomeTeam"] == team]

        home_goals_against = home_games["FTAG"].sum()
        home_shots_against = home_games["AS"].sum()

        away_games = df_premier[df_premier["AwayTeam"] == team]

        away_goals_against = away_games["FTHG"].sum()
        away_shots_against = away_games["HS"].sum()

        records.append({
            "Team": team,
            "Games": len(home_games) + len(away_games),
            "Shots Allowed Home": home_shots_against,
            "Goals Allowed Home": home_goals_against,
            "Home Opp Shots per Goal": home_shots_against / home_goals_against if home_goals_against > 0 else 0,
            "Home Opp Shots per Game": home_shots_against / (len(home_games) if len(home_games) > 0 else 1),
            "Shots Allowed Away": away_shots_against,
            "Goals Allowed Away": away_goals_against,
            "Away Opp Shots per Goal": away_shots_against / away_goals_against if away_goals_against > 0 else 0,
            "Away Opp Shots per Game": away_shots_against / (len(away_games) if len(away_games) > 0 else 1)
        })

    shots_against = pd.DataFrame(records)

    shots_against["Home Opp Shots per Goal"] = shots_against["Home Opp Shots per Goal"].round(
        2)
    shots_against["Home Opp Shots per Game"] = shots_against["Home Opp Shots per Game"].round(
        2)
    shots_against["Away Opp Shots per Goal"] = shots_against["Away Opp Shots per Goal"].round(
        2)
    shots_against["Away Opp Shots per Game"] = shots_against["Away Opp Shots per Game"].round(
        2)

    return shots_against


# Create a shots on target table
def create_shots_target_table(url):
    df_premier = pd.read_csv(url)

    teams = sorted(
        set(df_premier["HomeTeam"]) |
        set(df_premier["AwayTeam"])
    )

    records = []

    for team in teams:
        home_games = df_premier[df_premier["HomeTeam"] == team]

        home_sot = home_games["HST"].sum()
        home_shots_for = home_games["HS"].sum()

        away_games = df_premier[df_premier["AwayTeam"] == team]

        away_sot = away_games["AST"].sum()
        away_shots_for = away_games["AS"].sum()

        records.append({
            "Team": team,
            "Games": len(home_games) + len(away_games),
            "Shots on Target Home": home_sot,
            "Percent SOT Home": home_sot / home_shots_for if home_shots_for > 0 else 0,
            "Shots on Target Away": away_sot,
            "Percent SOT Away": away_sot / away_shots_for if away_shots_for > 0 else 0,
        })

    sot = pd.DataFrame(records)

    sot["Percent SOT Home"] = sot["Percent SOT Home"].round(2)
    sot["Percent SOT Away"] = sot["Percent SOT Away"].round(2)

    return sot


# Create a shots on target against table
def create_shots_target_against_table(url):
    df_premier = pd.read_csv(url)

    teams = sorted(
        set(df_premier["HomeTeam"]) |
        set(df_premier["AwayTeam"])
    )

    records = []

    for team in teams:
        home_games = df_premier[df_premier["HomeTeam"] == team]

        home_sot_against = home_games["AST"].sum()
        home_shots_against = home_games["AS"].sum()

        away_games = df_premier[df_premier["AwayTeam"] == team]

        away_sot_against = away_games["HST"].sum()
        away_shots_against = away_games["HS"].sum()

        records.append({
            "Team": team,
            "Games": len(home_games) + len(away_games),
            "SOT Allowed Home": home_sot_against,
            "Percent SOT Allowed Home": home_sot_against / home_shots_against if home_shots_against > 0 else 0,
            "SOT Allowed Away": away_sot_against,
            "Percent SOT Allowed Away": away_sot_against / away_shots_against if away_shots_against > 0 else 0,
        })

    sot_against = pd.DataFrame(records)

    sot_against["Percent SOT Allowed Home"] = sot_against["Percent SOT Allowed Home"].round(
        2)
    sot_against["Percent SOT Allowed Away"] = sot_against["Percent SOT Allowed Away"].round(
        2)

    return sot_against

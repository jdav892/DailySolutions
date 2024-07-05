def uefa_euro_2016(teams, scores):
    team1, team2 = teams
    score1, score2 = scores
    if score1 > score2:
        result = f"{team1} won!"
    elif score1 < score2:
        result = f"{team2} won!"
    else:
        result = "teams played draw." 
    
    return f"At match {team1} - {team2}, {result}"
group = [("Brazil", 3, 0, 0), ("Japan", 1, 2, 0), ("Spain", 2, 0, 1), ("Ghana", 0, 1, 2)]

filtered_teams = list(filter(lambda t: (t[1] * 3 + t[2]) >= 6 and t[3] <= 1, group))

filtered_teams.sort(key=lambda t: t[1] * 3 + t[2], reverse=True)

print("Advancing to knockouts:")
for team, wins, draws, losses in filtered_teams:
    points = wins * 3 + draws
    print(f"{team} - {points} pts")
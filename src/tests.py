# ## Testing Celtics vs Bucks
# # Creating players
# tatum = Player("Tatum", "6'5", "SF")
# brown = Player("Brown", "6'6", "SG")
# smart = Player("Smart", "6'4", "PG")
# horford = Player("Horford", "6'10", "C")
# white = Player("White", "6'4", "PG")

# giannis = Player("Giannis", "6'11", "PF")
# middleton = Player("Middleton", "6'7", "SF")
# holiday = Player("Holiday", "6'3", "PG")
# lopez = Player("Lopez", "7'0", "C")
# portis = Player("Portis", "6'10", "PF")

# # Creating teams
# celtics = Team('Boston', 'Celtics')
# bucks = Team('Milwaukee', 'Bucks')

# # Adding players to the Celtics
# celtics.add_player(tatum)
# celtics.add_player(brown)
# celtics.add_player(smart)
# celtics.add_player(horford)
# celtics.add_player(white)

# # Adding players to the Bucks
# bucks.add_player(giannis)
# bucks.add_player(middleton)
# bucks.add_player(holiday)
# bucks.add_player(lopez)
# bucks.add_player(portis)

# # Simulating game 1 between Celtics and Bucks
# game1 = Game(celtics, bucks)
# game1.sim_game()

# # Printing the final score
# print(game1.get_final_score())

# # Printing the winning team
# print(f"The winner is: {game1.winner.team_name}")
# print(celtics.record)

# # Simulating game 2 between Celtics and Bucks
# game2 = Game(celtics, bucks)
# game2.sim_game()

# # Printing the final score
# print(game2.get_final_score())

# # Printing the winning team
# print(f"The winner is: {game2.winner.team_name}")
# print(celtics.record)



# Create players for each team
# Lakers Players
from main import Player, Team, Season, Game


lebron = Player("LeBron James", "6'9", "SF")
davis = Player("Anthony Davis", "6'10", "PF")
russell = Player("D\'Angelo Russell", "6'4", "PG")
reeves = Player("Austin Reaves", "6'5", "SG")
vanderbilt = Player("Jarred Vanderbilt", "6'9", "PF")

# Warriors Players
curry = Player("Stephen Curry", "6'2", "PG")
thompson = Player("Klay Thompson", "6'6", "SG")
green = Player("Draymond Green", "6'6", "PF")
wiggins = Player("Andrew Wiggins", "6'7", "SF")
looney = Player("Kevon Looney", "6'9", "C")

# Celtics Players
tatum = Player("Jayson Tatum", "6'8", "SF")
brown = Player("Jaylen Brown", "6'6", "SG")
horford = Player("Al Horford", "6'9", "C")
smart = Player("Marcus Smart", "6'4", "PG")
white = Player("Derrick White", "6'4", "SG")

# Create Teams
lakers = Team("Los Angeles", "Lakers")
warriors = Team("Golden State", "Warriors")
celtics = Team("Boston", "Celtics")

# Add players to teams
for player in [lebron, davis, russell, reeves, vanderbilt]:
    lakers.add_player(player)

for player in [curry, thompson, green, wiggins, looney]:
    warriors.add_player(player)

for player in [tatum, brown, horford, smart, white]:
    celtics.add_player(player)



# Initialize season with 2 games per matchup
season = Season([lakers, warriors, celtics], games_per_matchup=2)

# Check the schedule length
assert len(season.schedule) == 6, "Schedule should contain 6 games (3 matchups * 2 games each)."
print("Schedule creation test passed.")

# Simulate the season
season.simulate_season()

# Get standings
standings = season.get_standings()

# Check that standings reflect each team’s games played
total_games_played = sum(record['Wins'] + record['Losses'] for record in season.standings.values())
assert total_games_played == len(season.schedule), "Total games in standings should match the schedule."
print("Season simulation and standings update test passed.")


# Check if each team has the correct number of games in standings
for team_name, record in season.standings.items():
    games_played = record['Wins'] + record['Losses']
    assert games_played == 4, f"Each team should play 4 games in a 3-team, 2-game-per-matchup season."
print("Win/loss consistency test passed.")



# Verify the standings are sorted by wins
sorted_standings = season.get_standings()
wins = [record['Wins'] for team, record in sorted_standings]
assert wins == sorted(wins, reverse=True), "Standings should be sorted by wins in descending order."
print("Standings sorting test passed.")


# Single team edge case
solo_team = Team("Los Angeles", "Solo Lakers")
solo_season = Season([solo_team])

# Check that no games are scheduled
assert len(solo_season.schedule) == 0, "Schedule should be empty when only one team is in the season."
print("Single team edge case test passed.")

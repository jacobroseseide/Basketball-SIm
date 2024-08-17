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
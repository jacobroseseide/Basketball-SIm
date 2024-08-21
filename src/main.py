# --------------- Player Class -------------
class Player:
    def __init__(self, name, height, position, current_stats=None, games=0):
        self._name = name
        self._height = height
        self._position = position
        self.stats = current_stats if current_stats else {
            'Points': 0, 'Rebounds': 0, 
            'Assists': 0, 'Steals': 0
        }
        self.games_played = games

    # properties of a given player (instead of getters)
    @property
    def name(self):
        return self._name
    
    @property
    def height(self):
        return self._height
    
    @property
    def position(self):
        return self._position
    
    # SETTERS

    # Adds Points to Stats
    def add_points(self, points_scored):
        if points_scored < 0 or isinstance(points_scored,float):
            raise TypeError("Must be a whole, positive integer")
        self.stats['Points'] += points_scored
    
    # Adds Rebounds to Stats
    def add_rebounds(self, rebound):
        if rebound < 0 or isinstance(rebound,float):
            raise TypeError("Must be a whole, positive integer")
        self.stats['Rebounds'] += rebound
    
    # Adds Assists to Stats
    def add_assists(self, assist):
        if assist < 0 or isinstance(assist,float):
            raise TypeError("Must be a whole, positive integer")
        self.stats['Assists'] += assist

    # Adds Steals to Stats
    def add_steals(self, steal):
        if steal < 0 or isinstance(steal,float):
            raise TypeError("Must be a whole, positive integer")
        self.stats['Steals'] += steal

    # Change position if needed (the game is evolving!!)
    def change_position(self, new_position):
        self._position = new_position

    # Reset Stats
    def reset_stats(self):
        self.stats = {
            'Points': 0, 'Rebounds': 0, 
            'Assists': 0, 'Steals': 0
        }
        self.games_played = 0
    
    # Method to increment games played
    def play_game(self, points=0, rebounds=0, assists=0, steals=0):
        self.games_played += 1
        self.add_points(points)
        self.add_rebounds(rebounds)
        self.add_assists(assists)
        self.add_steals(steals)
    
    # Per Game Stats Calculations
    @property
    def points_per_game(self):
        return self.stats['Points'] / self.games_played if self.games_played > 0 else 0
    
    @property
    def rebounds_per_game(self):
        return self.stats['Rebounds'] / self.games_played if self.games_played > 0 else 0
    
    @property
    def assists_per_game(self):
        return self.stats['Assists'] / self.games_played if self.games_played > 0 else 0
    @property
    def steals_per_game(self):
        return self.stats['Steals'] / self.games_played if self.games_played > 0 else 0

    # GETTERS
    
    # Get total stats
    def get_stats(self):
        return self.stats

    # Get points
    def get_points(self):
        return self.stats['Points']
    
    # Get rebounds
    def get_rebounds(self):
        return self.stats['Rebounds']
    
    # Get assists
    def get_assists(self):
        return self.stats['Assists']
    
    # Get steals
    def get_steals(self):
        return self.stats['Steals']


#------------------ Team Class ---------------------
class Team:
    def __init__(self, city, team_name):
        self.city = city
        self.team_name = team_name
        self.players = []
        self.record = {'W': 0, 'L': 0}
        self.starters = {}
    
    # add player to roster
    def add_player(self, player):
        if len(self.players) >= 15:
            raise ValueError("Roster is full")
        if player in self.players:
            raise ValueError(f"Player {player.name} is already on the team.")
        self.players.append(player)

    # cut player
    def remove_player(self,player_name):
        if len(self.players) <= 12:
            raise ValueError("Roster must have at least 12 players")
        # update players list by adding players that don't have input players name
        self.players = [player for player in self.players if player.name != player_name]
        # Also remove from starters if necessary
        self.starters = {position: p for position, p in self.starters.items() if p.name != player_name}

    # add win
    def add_win(self):
        self.record['W'] += 1
    
    # add loss
    def add_loss(self):
        self.record['L'] += 1

    # add starting 5
    def set_starters(self,starters):
        if len(starters) != 5:
            raise ValueError("Starting five must consist of exactly 5 players")
        # unique positions
        if len(set(starters.keys())) != 5:
            raise ValueError("Each position must be unique in the starting five")
        self.starters = starters

    # get starter by position
    def get_starter_by_position(self, position):
        return self.starters.get(position, None)

    # get total team stats
    def get_team_stats(self):
        team_stats = {'Points': 0, 'Rebounds': 0, 'Assists': 0, 'Steals': 0}
        for player in self.players:
            for stat in team_stats:
                team_stats[stat] += player.stats[stat]
        return team_stats
    
    # change starter at certain position
    def change_starter(self,position,player):
        if position not in self.starters:
            raise ValueError(f"No starter set for position: {position}")
        self.starters[position] = player


#------------------ Game Class ---------------------
import random

class Game:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        self.score1 = 0
        self.score2 = 0
        self.winner = None

    # calculate team strength based on weighted stats
    def calculate_team_strength(self, team):
        team_stats = team.get_team_stats()
        strength = (team_stats['Points'] * 0.5 + team_stats['Rebounds'] * 0.2 +
                    team_stats['Assists'] * 0.2 + team_stats['Steals'] * 0.1)
        return strength

    # method to sim game
    def sim_game(self):
        strength1 = self.calculate_team_strength(self.team1)
        strength2 = self.calculate_team_strength(self.team2)
        
        # Simulate scoring for team 1
        for player in self.team1.players:
            base_score = 25  # You can adjust this base score as needed
            points_scored = max(0, int((player.points_per_game or base_score) * random.uniform(0.8, 1.2)))
            self.score1 += points_scored
            player.add_points(points_scored)
        
        # Simulate scoring for team 2
        for player in self.team2.players:
            points_scored = max(0, int((player.points_per_game or base_score) * random.uniform(0.8, 1.2)))
            self.score2 += points_scored
            player.add_points(points_scored)    

        if self.score1 > self.score2:
            self.winner = self.team1
            self.team1.add_win()
            self.team2.add_loss()
        elif self.score1 < self.score2:
            self.winner = self.team2
            self.team1.add_loss()
            self.team2.add_win()
        else:
            # Tie, so we do overtime by randomly picking a winner
            print("The game is tied, running overtime...")
            self.winner = random.choice([self.team1, self.team2])
            self.winner.add_win()
            if self.winner == self.team1:
                self.team2.add_loss()
            else:
                self.team1.add_loss()
    

    def get_final_score(self):
        return f"{self.team1.team_name}: {self.score1}, {self.team2.team_name}: {self.score2}"


    ## Testing Celtics vs Bucks
# Creating players
tatum = Player("Tatum", "6'5", "SF")
brown = Player("Brown", "6'6", "SG")
smart = Player("Smart", "6'4", "PG")
horford = Player("Horford", "6'10", "C")
white = Player("White", "6'4", "PG")

giannis = Player("Giannis", "6'11", "PF")
middleton = Player("Middleton", "6'7", "SF")
holiday = Player("Holiday", "6'3", "PG")
lopez = Player("Lopez", "7'0", "C")
portis = Player("Portis", "6'10", "PF")

# Creating teams
celtics = Team('Boston', 'Celtics')
bucks = Team('Milwaukee', 'Bucks')

# Adding players to the Celtics
celtics.add_player(tatum)
celtics.add_player(brown)
celtics.add_player(smart)
celtics.add_player(horford)
celtics.add_player(white)

# Adding players to the Bucks
bucks.add_player(giannis)
bucks.add_player(middleton)
bucks.add_player(holiday)
bucks.add_player(lopez)
bucks.add_player(portis)

# Simulating game 1 between Celtics and Bucks
game1 = Game(celtics, bucks)
game1.sim_game()

# Printing the final score
print(game1.get_final_score())

# Printing the winning team
print(f"The winner is: {game1.winner.team_name}")
print(celtics.record)

# Simulating game 2 between Celtics and Bucks
game2 = Game(celtics, bucks)
game2.sim_game()

# Printing the final score
print(game2.get_final_score())

# Printing the winning team
print(f"The winner is: {game2.winner.team_name}")
print(celtics.record)
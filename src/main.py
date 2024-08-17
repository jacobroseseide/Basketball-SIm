# --------------- Player Class -------------
class Player:
    def __init__(self, name, height, position, current_stats=None):
        self._name = name
        self._height = height
        self._position = position
        self.stats = current_stats if current_stats else {
            'Points': 0, 'Rebounds': 0, 
            'Assists': 0, 'Steals': 0
        }

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
            # Weighted random points based on team strength
            points_scored = max(10, random.randint(int(strength1 * 0.8), int(strength1 * 1.2)))
            self.score1 += points_scored
            player.add_points(points_scored)
        
        # Simulate scoring for team 2
        for player in self.team2.players:
            points_scored = max(10, random.randint(int(strength2 * 0.8), int(strength2 * 1.2)))
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

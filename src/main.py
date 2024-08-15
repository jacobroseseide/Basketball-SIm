# Class to create player
class Player:
    def __init__(self, name, height, position):
        self.name = name
        self.height = height
        self.position = position
        self.stats = {
            'Points': 0, 'Rebounds': 0, 
            'Assists': 0, 'Steals': 0
        }
    
    # SETTERS

    # Adds Points to Stats
    def addPoints(self, points_scored):
        self.stats['Points'] += points_scored
    
    # Adds Rebounds to Stats
    def addRebounds(self, rebound):
        self.stats['Rebounds'] += rebound
    
    # Adds Assists to Stats
    def addAssists(self, assist):
        self.stats['Assists'] += assist

    # Adds Steals to Stats
    def addSteals(self, steal):
        self.stats['Steals'] += steal

    # Change position if needed (the game is evolving!!)
    def changePosition(self, new_position):
        self.position = new_position

    # GETTERS
        
    # Get name
    def getName(self):
        return self.name
    
    # Get height
    def getHeight(self):
        return self.height
    
    # Get position
    def getPosition(self):
        return self.position
    
    # Get total stats
    def getStats(self):
        return self.stats

    # Get points 
    def getPoints(self):
        return self.stats['Points']
    
    # Get rebounds
    def getRebounds(self):
        return self.stats['Rebounds']
    
    # Get assists
    def getAssists(self):
        return self.stats['Assists']
    
    # Get steals
    def getSteals(self):
        return self.stats['Steals']




class Team:
    def __init__(self, team_name):
        self.team_name = team_name
        self.players = []
        self.record = {'W': 0, 'L': 0}

class Game:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        self.score1 = 0
        self.score2 = 0
        self.winner = None

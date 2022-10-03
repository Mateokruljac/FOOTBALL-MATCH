import random

class Team:

    def __init__(self,name:str):
        """ 
        This method retruns the football team name.
        Home team and away team uses same class Team.
        Make instance for each team separately
        For instance: 
           first team instance:
                   chelsea = Team(name = Chelsea)
           second team instance:
                   arsenal = Team(name = Arsenal)        
        """
        self.name = name 
        
        
class Score:
    """ 
    Each team has 0 score(s) at the begging of the match 
    """
    home = 0 #started score of first team 
    away = 0 #started score of second team
    
    def first_team_goal(self):
        """ 
        This method will asssign yellow card to first team,
        if random.randint is equal to desired number. 
        Returns boolean value (True/False)
        """
        return random.randint(1,40) == 4
    
    def second_team_goal(self):
        """ 
        This method will asssign yellow card to second team,
        if random.randint is equal to desired number. 
        Returns boolean value (True/False)
        """
        return random.randint(1,40) == 9
    
    
class Corner: 
    """ 
    Each team has 0 corner(s) at the beggining of the match
    """
    home = 0 #started corner of first team 
    away = 0 #started corner of second team

    def first_team_corner(self):
        """ 
        This method will asssign yellow card to first team,
        if random.randint is equal to desired number. 
        Returns boolean value (True/False)
        """
        return random.randint(1,40) == 4
    
    def second_team_corner(self):
        """ 
        This method will asssign yellow card to second team,
        if random.randint is equal to desired number. 
        Returns boolean value (True/False)
        """
        return random.randint(1,40) == 9
        

class Shoot: 
    """ 
    Each team has 0 shoot(s) at the beggining of the match
    """
    home = 0 #started shoot of first team 
    away = 0 #started shoot of second team
    
    def first_team_shoot(self):
        """ 
        This method will asssign yellow card to first team,
        if random.randint is equal to desired number. 
        Returns boolean value (True/False)
        """
        return random.randint(1,40) == 4
    
    def second_team_shoot(self):
        """ 
        This method will asssign yellow card to second team,
        if random.randint is equal to desired number. 
        Returns boolean value (True/False)
        """
        return random.randint(1,40) == 9
        


    
class YellowCard: 
    """ 
    Each team has 0 yellow card at the beggining of the match 
    """
    home = 0  # for first team 
    away = 0  # for second team 
    
    def first_team_gets_yellow_card(self):
        """ 
        This method will asssign yellow card to first team,
        if random.randint is equal to desired number. 
        Returns boolean value (True/False)
        """
        return random.randint(1,40) == 4
    
    def second_team_gets_yellow_card(self):
        """ 
        This method will asssign yellow card to second team,
        if random.randint is equal to desired number. 
        Returns boolean value (True/False)
        """
        return random.randint(1,40) == 9
        

class RedCard:
    """ 
    Each team has 0 red card at the beggining of the match 
    """
    home = 0  # for first team 
    away = 0  # for second team 
    
    def first_team_gets_red_card(self):
        """ 
        This method will asssign red card to first team,
        if random.randint is equal to desired number. 
        Returns boolean value (True/False)
        """
        return random.randint(1,80) == 4
    
    def second_team_gets_red_card(self):
        """ 
        This method will asssign red card to second team,
        if random.randint is equal to desired number. 
        Returns boolean value (True/False)
        """
        return random.randint(1,80) == 9
        
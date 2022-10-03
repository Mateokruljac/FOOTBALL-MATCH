import time 
from before_match import Score,YellowCard,RedCard,Corner,Shoot

class Match():
    
    def __init__(self,home,away):
        """ """
        self.home = home
        self.away = away 
        self.score = Score()
        self.corner = Corner()
        self.yellow_card = YellowCard()
        self.red_card = RedCard()
        self.minute = 0
        self.shoot = Shoot()
        self.home.yellow = 0
        self.home.red = 0
        self.away.yellow = 0 
        self.away.red  = 0 
        
    
    def start_match (self):
        while self.minute < 91: 
            if self.minute == 0:
                print("------------------")
                print("Match started!")
            print(f"{self.home.name}          VS       {self.away.name}       MINUTE")
            
            #instances of Score class and method 
            first_team_goal = self.score.first_team_goal()
            second_team_goal = self.score.second_team_goal()
            
            #instances of Corner class and method 
            first_team_corner = self.corner.first_team_corner()
            second_team_corner = self.corner.second_team_corner()
            
            #instances of Shoot class and method 
            first_team_shoot = self.shoot.first_team_shoot()
            second_team_shoot = self.shoot.second_team_shoot()
            
            #instances of RedCard class and method 
            first_team_red_card = self.red_card.first_team_gets_red_card()
            second_team_red_card = self.red_card.second_team_gets_red_card()
            
            #instances of YellowCard class and method 
            first_team_yellow_card = self.yellow_card.first_team_gets_yellow_card()
            second_team_yellow_card = self.yellow_card.second_team_gets_yellow_card()
            
            
            #first team and second team scored goal 
            if first_team_goal:
                self.score.home += 1 
            if second_team_goal:
                self.score.away += 1    
            
            #first team and second team shooted a ball
            if first_team_shoot:
                self.shoot.away += 1    
            if second_team_shoot:
                self.shoot.away += 1  
             
            #first team and second team got a corner      
            if first_team_corner:
                self.corner.home += 1     
            if second_team_corner:
                self.corner.away += 1    
            
            #players of first or second team earned yellow card
            if first_team_yellow_card:
                self.yellow_card.home += 1 
            if second_team_yellow_card:
                self.yellow_card.away += 1 
                
            #players of first or second team earned yellow card
            if first_team_red_card:
                self.red_card.home += 1 
            if second_team_red_card:
                self.red_card.away += 1 
            
            print(f"{self.score.home}                :         {self.score.away}            {self.minute}")
            self.minute += 1 
            time.sleep(0.1)
            
            if self.minute == 46:
                print("HALF-TIME")
                time.sleep(2)
            
            #end match. print a winner 
            if self.minute > 90:
                if self.score.home > self.score.away: 
                    print(f"{self.home.name} is Winner!!!")
                elif self.score.home == self.score.away:
                    print("DRAW!!!")
                else:
                    print(f"{self.away.name} is Winner!")
            
from match import Match 
from your_choice import YourChoice
from login import Card

class FinallyBetting (Match,YourChoice,Card) :
    balance  = 0
    @classmethod
    def info(cls):
        return super().info()
    
    def check_amount(self):
        return super().check_amount()
    
    def start_match(self):
        return super().start_match()
 
    def finallybetting (self):   
        if self.choice_ == 1: # if your choice is that first team win
            if self.score.home > self.score.away:
                self.coeficcient = 0.180  
                self.new_balance = self.balance + self.amount + self.amount*self.coeficcient
                print("1 You win")
                return print(self.new_balance)

            else:
                print("1 You lost")
        if self.choice_ == 2:# look at BettingInfo.py
           if self.score.home < self.score.away:
               self.coeficcient = 0.190
               print("2 You win")
           else:
               print("2 You lost")
        
        if self.choice_ == 3:
           if self.corner.home > self.corner.away:
               self.coeficcient = 0.140
               print("3 You win")
           else:
               print("3You lost")
        
        if self.choice_ == 4:
            if self.corner.home < self.corner.away:
                self.coeficcient = 1.70
                print("4 You win")
            else:
               print("4 You lost") 
        
        if self.choice_ == 5:
            if self.home.yellow > self.away.yellow:
                self.coeficcient = 1.70
                print("5 You Win")
            else:
                print("5 You lost")
        
        if self.choice_ == 6:
            if self.home.yellow < self.away.yellow:
                self.coeficcient = 1.90
                print("6 You win")
            else:
                print("6 You lost")
        if self.choice_ == 7:
            if self.home.red == True:
                self.coeficcient = 3.60
                print("7 You win")
            else:
                print("7 You lost")
        if self.choice_ == 8:
            if self.home.red == True:
                self.coeficcient = 4.20
                print("8 You win")
            else:
                print("8 You lost") 
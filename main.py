from results import FinallyBetting
from before_match import Team
from match_info import BettingHouseName, Offer

#info about betting house and daily offer
betting_house_name = BettingHouseName()
offer = Offer()


#select teams
first_team = Team("Arsenal")
second_team = Team("Chelsea")
#run app
match = FinallyBetting(first_team,second_team)
match.info()
match.check_amount()
match.choice()
match.start_match()
match.finallybetting()


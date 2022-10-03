class EmailAddress:
    
    def check_email(self,email:str): 
        if email.count("@")  == 1:
            self.email_address = email.split("@")
            if ".hr" in self.email_address[1] or ".com" in self.email_address[1]:
               if email[1].islower() and email.count(" ") == 0 and self.email_address[1].split(".")[0] != "":
                   print(f"Welcome, {self.email_address[0]} !")
                   return self.email_address[0]  
               else:
                    print("1.Invalid Email address.Try with another or check your address!")
                    exit()   
            else:
                print("2.Invalid Email address.Try with another or check your address!")
                exit()
        else:
            print("3.Invalid Email address.Try with another or check your address!")
            exit()

class Card(EmailAddress):
    @classmethod
    def info (cls):
        email = input("Enter email: ")
        #username is provided by check_email method. This method is method
        #of EmailAddress class. Class Card inherits class EmailAddress
        cls.username = cls.check_email(cls,email=email)
        cls.balance = 1000
        print("Username:",cls.username)
        print("Balance",cls.balance)
        while True:  
          try:
              cls.amount = int(input("Enter amount: "))
              print(f"Amount: {cls.amount}")
              return cls.balance
              break
          except ValueError:
              print("Please use integer!")
    
    def check_amount (self):
        if self.amount <= self.balance:
            self.new_balance = self.balance - self.amount 
            print(f"New balance: {self.new_balance}")
        else:
            print("You do not have enough money!")
            exit()
        
            


class YourChoice:
    def choice (self):
        while True: 
          try:  
             self.choice_ = int(input("Select one option: "))
             break
          except ValueError:
              print("Please use number!")
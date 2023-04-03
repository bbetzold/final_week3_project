class Parking_Garage():
    
    def __init__(self,parkingSpaces, name):
        self.tickets_available = parkingSpaces
        self.parkingSpaces = parkingSpaces
        self.name = name
        self.id_name = {}


    def takeTicket(self):
        
        license_id = input("\nWhat's your license plate number?: ")
        guest_name = input("Whats your name? ")
    
        self.id_name[license_id] = guest_name           
        self.tickets_available -= 1
        for key, value in self.id_name.items():
            print(f"\n {value.title()}, your license plate number is {key.upper()} and you purchased 1 ticket. ")
        
    def returnTicket(self):
        plate_number = input("\nWhat's your license plate number? ")
        if plate_number not in self.id_name:
            print(f"Try again - we have no record of plate {plate_number.upper()}.")
        else:
            self.tickets_available += 1
            del self.id_name[plate_number]
            self.checkoutTicket()


    def showTicketavailable(self): 
            print(f'\n{self.tickets_available} tickets available.') 
            print(self.id_name)
      
    def checkoutTicket(self):
        while True:
            payment = input("Please pay your fee of $15.00 (Type: 15.00): ")
            if payment != "15.00":
                print("Incorrect amount.")
                self.checkoutTicket()
            else:
                print(f" \nThanks for parking at {self.name}.\nHave a great day!")
            break
    
    def showOptions(self):
        print(f"""
        Here are your options:
        [1] Enter {self.name}
        [2] Exit {self.name}
        [3] Show Available Tickets
        [4] Confirm Exit and Print Receipt    
        """)
                
                
    def run(self):
           
    
        while True:

            try:
            
                self.showOptions()
                response = input(f"\nWelcome to {self.name}! It is $15.00 per day to park! \nPlease enter a number option? ")

                if response == '1':
                    self.takeTicket()

                elif response == '2':
                    self.returnTicket()
                    
                    
                elif response == '3':
                    self.showTicketavailable()

                elif response == '4':
                    print("\nHave a great day! ")
                    break

                else:
                    print("Invalid entry. Please try again, doofus.")

            except:
                    print("""
                    Apparently you found a way to make this not work. Please do better next time.
                    Your entry should be a number between 1 and 4.
                    """)



ethans_Garage = Parking_Garage(100, "ELB's Cool-Ass Garage")
            
ethans_Garage.run()
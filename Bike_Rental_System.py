  
import datetime

print(' \n     ========== Welcome to pen Bike Rental Service ==========')
class openBikes:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock
        self.rent = {}
        self.money = 0
        self.time = ''
        self.selectedPlan = 0
        self.cuntr = 0

    def showRecords(self):
        print(self.rent)

    def rentBikeHourly(self, name, howMuch):
        print(f"Available Bikes in inventory {self.stock}")
        if howMuch > self.stock:
            print(f"Bike shortage! You can have max {self.stock} bikes.")

        else:
            self.rent.update({name:{"hourly":howMuch}})
            print("Bike rented successfully!")
            self.stock -= howMuch
            self.cuntr = howMuch
            self.selectedPlan = 1
            self.money = 5 * howMuch
            xt = datetime.datetime.now()
            self.time = xt.strftime("%s")
            print(f"\nBikes now available in enventory - {self.stock}")
            input("press any key to continue:")

    def rentBikeDaily(self, name, howMuch):
        print(f"Available Bikes in inventory {self.stock}")
        if howMuch > self.stock:
            print(f"Bike shortage! You can have max {self.stock} bikes.")

        else:
            self.rent.update({name:{"daily":howMuch}})
            print("Bike rented successfully!")
            self.stock -= howMuch
            self.cuntr = howMuch
            self.selectedPlan = 2
            self.money = 20 * howMuch
            xt = datetime.datetime.now()
            self.time = xt.strftime("%s")
            print(f"\nBikes now available in enventory - {self.stock}")
            input("press any key to continue:")

    def rentBikeWeekly(self, name, howMuch):
        print(f"Available Bikes in inventory {self.stock}")
        if howMuch > self.stock:
            print(f"Bike shortage! You can have max {self.stock} bikes.")

        else:
            self.rent.update({name:{"weekly":howMuch}})
            print("Bike rented successfully!")
            self.stock -= howMuch
            self.cuntr = howMuch
            self.selectedPlan = 3
            self.money = 100 * howMuch
            xt = datetime.datetime.now()
            self.time = xt.strftime("%s")
            print(f"\nBikes now available in enventory - {self.stock}")
            input("press any key to continue:")


    def billing(self, name):
        if name in self.rent.keys():
            self.rent.pop(name)
            xt = datetime.datetime.now()
            xtime = xt.strftime("%s")
            ftime = int(xtime)-int(self.time)
            if self.selectedPlan == 1:
                self.money = ftime*5

            elif self.selectedPlan == 2:
                self.money = ftime*20

            elif self.selectedPlan == 3:
                self.money = ftime*100

            if self.cuntr >= 3:
                x = self.money/10*3
                self.money = x

            print(f"Thanks for using our Service {name.upper()} \nHere is your bill ({self.money} $)")
            self.stock+=self.cuntr

        else:
            print(f"\nsorry {name} not in record")
            input("press any key to continue:")
        # return ftime


if __name__ == '__main__':
    Bikers = openBikes('Open Bike Rental Service', 100)

    while(True):
        print("""
           ----------------------------------------\n
                1 -- for Rent Bike Hourly - 5$.
                2 -- for Rent Daily - 20$.
                3 -- for Rent Weekly - 100$.
                4 -- for Return Bike. 
                5 -- for show customers record. 
                6 -- to quit the programm\n
           ----------------------------------------
        """)
        print(f"Available Bikes in inventory {Bikers.stock}\n")
        userChoice = int(input("Enter your Choice: "))

        if userChoice == 1:
            bqunt = int(input("How much bikes you want: "))
            if bqunt > Bikers.stock:
                print(f"Sorry we only have {Bikers.stock} in enventory")

            else:
                uname = input("Enter your Name: ")
                Bikers.rentBikeHourly(uname, bqunt)

        elif userChoice == 2:
            bqunt = int(input("How much bikes you want: "))
            if bqunt > Bikers.stock:
                print(f"Sorry we only have {Bikers.stock} in enventory")

            else:
                uname = input("Enter your Name: ")
                Bikers.rentBikeDaily(uname, bqunt)

        elif userChoice == 3:
            bqunt = int(input("How much bikes you want: "))
            if bqunt > Bikers.stock:
                print(f"Sorry we only have {Bikers.stock} in enventory")

            else:
                uname = input("Enter your Name: ")
                Bikers.rentBikeWeekly(uname, bqunt)

        elif userChoice == 4:
            uname = input("Enter your Name: ")
            Bikers.billing(uname)

        elif userChoice == 5:
            Bikers.showRecords()

        elif userChoice == 6:
            print(f"Thanks for visiting -{Bikers.name}-")
            quit()
        
        else:
            print("Not a valid option :( try again!")
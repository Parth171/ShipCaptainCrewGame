"""
title: Game Engine
author: Parth Sakpal
date-created: 12/04/2023
"""
import player
from player import Player
from dice import Dice
import tabulate

def startScreen():
    print("welcome to ship captain crew")

def getPlayers():
    PLAYERS = []
    INPUT = input("how many players playing? (2-5): ") # implement error check for this



class Multiplayer:

    def __init__(self, PLAYER1:player.Player, PLAYER2:player.Player):
        self.player1 = PLAYER1
        self.player2 = PLAYER2
        self.p1Count = 3
        self.p2Count = 3
        self.allFound = False
        self.shipFound = False
        self.captainFound = False
        #self.crewFound = False

    def run(self):

        print(f"{self.player1} roll. Press enter to roll")
        self.player1.createDices(5)

        while self.p1Count > 0:


            input("press enter to continue....")
            ROLL = self.player1.rollActiveDices()

            print(ROLL)

            self.p1Count = self.p1Count - 1

            if not self.shipFound:
                if 6 in ROLL:
                    print("ship found")
                    self.player1.createDices(4)
                    self.shipFound = True


            if self.shipFound == True:
                if not self.captainFound:
                    if 5 in ROLL:
                        print("captain found")
                        self.player1.createDices(3)
                        self.captainFound = True

            if self.captainFound == True:
                if not self.allFound:
                    if 4 in ROLL:
                        print("crew found")
                        self.player1.createDices(2)
                        self.allFound = True



            if self.allFound == True:



                if self.p1Count > 1:
                    self.player1.createDices(2)
                    input("press enter to continue....")
                    GOLD_ROLL = self.player1.rollActiveDices()
                    print(GOLD_ROLL)


                    self.player1.playerGold = sum(GOLD_ROLL)
                    print(self.player1.playerGold)

                self.p1Count -= 1

                INPUT = input("ROLL AGAIN? ")

                if INPUT == 'Y':
                    GOLD_ROLL = self.player1.rollActiveDices()

                    print(GOLD_ROLL)

                    self.player1.playerGold = sum(GOLD_ROLL)
                    print(self.player1.playerGold)
                    exit()

                elif INPUT == "N":
                    print(self.player1.playerGold)
                    exit()

        print(self.player1.playerGold)









class SinglePlayer:
    pass


if __name__ == "__main__":

    P1 = Player("Parth")
    p2 = Player("Moksh")

    GAME = Multiplayer(P1, p2)
    GAME.run()

    """if self.p1Count > 1:

                 self.player1.createDices(2)
                 input("press enter to continue....")
                 self.player1.rollActiveDices()
                 print(self.player1.getRoll())

                 self.player1.playerGold = sum(self.player1.getRoll())
                 print(self.player1.playerGold)

                 self.p1Count -= 1

                 INPUT = input("ROLL AGAIN? ")

                 if INPUT == 'Y':
                     input("press enter to continue....")
                     self.player1.rollActiveDices()
                     print(self.player1.getRoll())

                     self.player1.playerGold = sum(self.player1.getRoll())
                     print(self.player1.playerGold)

                 elif INPUT == "N":
                     return self.player1.playerGold"""

"""if 6 in ROLL and 5 in ROLL and 4 in ROLL:
           print("All found")
           self.Found = True

       elif 6 in ROLL and 5 in ROLL:
           print("Ship and Captain found")
           self.shipFound = True
           self.captainFound = True

       elif 6 in ROLL and 5 not in ROLL:
           print("ship found")
           self.shipFound = True

       if self.shipFound == True:

           self.player1.createDices(4)

           if 5 in ROLL and 4 in ROLL:  
               print("captain and crew found")
               self.captainFound = True
               self.crewFound = True

           if 5 in ROLL:
               print("captain found")
               self.captainFound

       if self.captainFound == True:

           if 4 in ROLL:
               print("crew found")
               self.allFound = True"""
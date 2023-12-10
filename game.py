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



class Play:

    def __init__(self, PLAYER:player.Player):
        self.player = PLAYER

        self.pCount = 3
        self.allFound = False
        self.shipFound = False
        self.captainFound = False

    def run(self):

        print(f"{self.player} roll. Press ENTER to begin the round!")
        self.player.createDices(5)

        while self.pCount > 0:


            input("Press ENTER to roll you dice.")
            ROLL = self.player.rollActiveDices()

            print(f"Your Roll was: {ROLL}")

            self.pCount = self.pCount - 1

            if not self.shipFound:
                if 6 in ROLL:
                    print("\nship found\n")
                    self.player.createDices(4)
                    self.shipFound = True


            if self.shipFound == True:
                if not self.captainFound:
                    if 5 in ROLL:
                        print("\ncaptain found\n")
                        self.player.createDices(3)
                        self.captainFound = True

            if self.captainFound == True:
                if not self.allFound:
                    if 4 in ROLL:
                        print("\ncrew found\n")
                        self.player.createDices(2)
                        self.allFound = True



            if self.allFound == True:

                while self.pCount > 1:

                    self.player.createDices(2)
                    input("Press ENTER to roll for gold!")
                    GOLD_ROLL = self.player.rollActiveDices()
                    print(GOLD_ROLL)


                    self.player.playerGold = sum(GOLD_ROLL)
                    print(self.player.playerGold)

                    self.pCount -= 1

                    INPUT = input("ROLL AGAIN? (Y/N): ")

                    if INPUT == "Y" or INPUT == "N":
                        pass
                    else:
                        print("Please enter Y or N.")
                        INPUT = input("ROLL AGAIN? (Y/N): ")

                    if INPUT == 'Y':
                        GOLD_ROLL = self.player.rollActiveDices()

                        print(f"Your New Roll: {GOLD_ROLL}")

                        self.player.playerGold = sum(GOLD_ROLL)
                        print(f"you got {self.player.playerGold} pieces of gold!")
                        return self.player.playerGold


                    if INPUT == "N":
                        if self.player.playerGold == 0:
                            print("Sorry you got no gold this round :(")
                            return 0
                        else:
                            print(f"you got {self.player.playerGold} pieces of gold!")
                            return self.player.playerGold



                if self.pCount == 1:
                    self.player.createDices(2)
                    input("Roll for Gold...")
                    GOLD_ROLL = self.player.rollActiveDices()
                    print(GOLD_ROLL)
                    self.player.playerGold = sum(GOLD_ROLL)
                    if self.player.playerGold == 0:
                        print("Sorry you got no gold this round :(")
                        return 0
                    else:
                        print(f"you got {self.player.playerGold} pieces of gold!")
                        return self.player.playerGold

        print("Sorry you got no gold this round :(")
        return 0

    def computer(self):

        input(f"Computers Roll. Press ENTER to begin the round!")
        self.player.createDices(5)

        while self.pCount > 0:

            ROLL = self.player.rollActiveDices()


            print("Computer Rolling....")
            print(f"Computer Rolled: {ROLL}")

            self.pCount = self.pCount - 1

            if not self.shipFound:
                if 6 in ROLL:
                    print("\nship found\n")
                    self.player.createDices(4)
                    self.shipFound = True


            if self.shipFound == True:
                if not self.captainFound:
                    if 5 in ROLL:
                        print("\ncaptain found\n")
                        self.player.createDices(3)
                        self.captainFound = True

            if self.captainFound == True:
                if not self.allFound:
                    if 4 in ROLL:
                        print("\ncrew found\n")
                        self.player.createDices(2)
                        self.allFound = True



            if self.allFound == True:

                while self.pCount > 1:

                    self.player.createDices(2)
                    input("Computer Rolling for Gold...")
                    GOLD_ROLL = self.player.rollActiveDices()
                    print(GOLD_ROLL)


                    self.player.playerGold = sum(GOLD_ROLL)
                    print(self.player.playerGold)

                    self.pCount -= 1

                    if self.player.playerGold < 6:

                        print("Computer Rolls Again!")


                        GOLD_ROLL = self.player.rollActiveDices()

                        print(f"Computer's New Roll: {GOLD_ROLL}")

                        self.player.playerGold = sum(GOLD_ROLL)
                        print(f"Computer got {self.player.playerGold} pieces of gold!")
                        return self.player.playerGold


                    else:
                        if self.player.playerGold == 0:
                            print("Computer got no gold this round :(")
                            return 0
                        else:
                            print(f"Computer got {self.player.playerGold} pieces of gold!")
                            return self.player.playerGold



                if self.pCount == 1:
                    self.player.createDices(2)
                    input("Computer Rolling for Gold...")
                    GOLD_ROLL = self.player.rollActiveDices()
                    print(GOLD_ROLL)
                    self.player.playerGold = sum(GOLD_ROLL)
                    if self.player.playerGold == 0:
                        print("Computer got no gold this round :(")
                        return 0
                    else:
                        print(f"Computer got {self.player.playerGold} pieces of gold!")
                        return self.player.playerGold

        print("Computer got no gold this round :(")
        return 0

    def winner(self, PLAYER1:player.Player, PLAYER2:player.Player):

        if PLAYER1.playerGold > PLAYER2.playerGold:
            return PLAYER1
        if PLAYER1.playerGold < PLAYER2.playerGold:
            return PLAYER2
        else:
            print("You Tied! Tie Break!!")




class threeRounds:

    def __init__(self, PLAYER1: player.Player, PLAYER2: player.Player):
        self.player1 = PLAYER1
        self.player2 = PLAYER2
        self.p1Gold = 0
        self.p2Gold = 0

    def intro(self):
        print("""
        ###

        Player one will take three turns
        Player two will take three turns

        """)

    def run(self):

        for i in range(3):
            self.p1Gold += Play(self.player1).run()

            self.p2Gold += Play(self.player2).run()



class SinglePlayer:

    def __init__(self, PLAYER:player.Player):
        self.player = PLAYER
        self.computer = Player("Computer")

    def run(self):

        Play(self.player).run()
        Play(self.computer).computer()








if __name__ == "__main__":

    P1 = Player("Parth")
    p2 = Player("Moksh")

    GAME = SinglePlayer(P1)
    GAME.run()





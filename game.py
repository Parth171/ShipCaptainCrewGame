"""
title: Game Engine Classes
author: Parth Sakpal
date-created: 12/04/2023
"""
import player
from player import Player


class Play:

    """
    This is the class that contains the logic for the game play.
    """

    def __init__(self, PLAYER:player.Player):
        self.player = PLAYER
        self.pCount = 3

        # Initially setting all these found to False and updates as they are found
        self.allFound = False
        self.shipFound = False
        self.captainFound = False

    def run(self):


        print(f"\n **{self.player}'s roll. ** ")
        self.player.createDices(5)

        while self.pCount > 0:


            input("\nPress ENTER to roll you dice.") # Gets user to press ENTER to maximize user engagement with the program
            ROLL = self.player.rollActiveDices()


            print(f"Your Roll was: {ROLL}")






            if not self.shipFound:
                if 6 in ROLL:
                    print("\nShip found! The Ship dice is held!\n")
                    self.player.createDices(4)
                    self.shipFound = True


            if self.shipFound == True:
                if not self.captainFound:
                    if 5 in ROLL:
                        print("\nCaptain found! The Captain dice is held!\n")
                        self.player.createDices(3)
                        self.captainFound = True

            if self.captainFound == True:
                if not self.allFound:
                    if 4 in ROLL:
                        print("\nCrew found! The Crew dice is held!\n")
                        self.player.createDices(2)
                        self.allFound = True



            if self.allFound == True:

                if self.pCount == 3:

                    self.player.createDices(2)
                    input("Press ENTER to roll for gold!")
                    GOLD_ROLL = self.player.rollActiveDices()
                    print(f"Your Gold Roll: {GOLD_ROLL}")


                    self.player.playerGold = sum(GOLD_ROLL)
                    print(self.player.playerGold)



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
                        print(f"You got {self.player.playerGold} pieces of gold this round!")
                        return self.player.playerGold


                    if INPUT == "N":

                        print(f"You got {self.player.playerGold} pieces of gold this round!")
                        return self.player.playerGold



                if self.pCount == 2:
                    self.player.createDices(2)
                    input("Press ENTER to roll for gold!")
                    GOLD_ROLL = self.player.rollActiveDices()
                    print(f"Your Gold Roll: {GOLD_ROLL}")
                    self.player.playerGold = sum(GOLD_ROLL)
                    print(f"You got {self.player.playerGold} pieces of gold!")
                    return self.player.playerGold

                if self.pCount == 1:
                    if len(self.player.activeDices) == 5:
                        self.player.activeDices.remove(6)
                        self.player.activeDices.remove(5)
                        self.player.activeDices.remove(4)
                        self.player.playerGold = sum(self.player.activeDices)
                    if len(self.player.activeDices) == 4:
                        self.player.activeDices.remove(5)
                        self.player.activeDices.remove(4)
                        self.player.playerGold = sum(self.player.activeDices)

                    if len(self.player.activeDices) == 3:
                        self.player.activeDices.remove(4)
                        self.player.playerGold = sum(self.player.activeDices)

                    print(f"You got {self.player.playerGold} pieces of gold!")
                    return self.player.playerGold

            self.pCount = self.pCount - 1



        print("\nSorry you used up all three rolls but this couldn't find all Three elements. You get no gold this round :(") # This is if the user gets no gold throughout the gameplay
        return 0

    def computer(self):
        """
        This method is for the single player gamemode and defines the gameplay of playing against a computer.
        """

        input(f"\nComputers Roll. Press ENTER to begin the round!")
        self.player.createDices(5)

        while self.pCount > 0:

            ROLL = self.player.rollActiveDices()


            print("Computer Rolling....")
            print(f"\nComputer Rolled: {ROLL}")

            self.pCount = self.pCount - 1

            if not self.shipFound:
                if 6 in ROLL:
                    print("\nShip found!\n")
                    self.player.createDices(4)
                    self.shipFound = True


            if self.shipFound == True:
                if not self.captainFound:
                    if 5 in ROLL:
                        print("\nCaptain found!\n")
                        self.player.createDices(3)
                        self.captainFound = True

            if self.captainFound == True:
                if not self.allFound:
                    if 4 in ROLL:
                        print("\nCrew found!\n")
                        self.player.createDices(2)
                        self.allFound = True



            if self.allFound == True:

                while self.pCount > 1:

                    self.player.createDices(2)
                    input("Computer Rolling for Gold...\n")
                    GOLD_ROLL = self.player.rollActiveDices()
                    print(f"Computer's Gold Roll: {GOLD_ROLL}")


                    self.player.playerGold = sum(GOLD_ROLL)
                    print(self.player.playerGold)

                    self.pCount -= 1

                    # Defines the logic for when the Computer should choose to re-roll
                    if self.player.playerGold < 6:

                        print("Computer Rolls Again!")


                        GOLD_ROLL = self.player.rollActiveDices()

                        print(f"Computer's New Gold Roll: {GOLD_ROLL}")

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
                    input("Press ENTER to Continue")
                    print("Computer Rolling for Gold...")
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

class bestOfThree:
    """
    Gameplay mode where two users play best of three to determine the winner
    """

    def __init__(self, PLAYER1: player.Player, PLAYER2: player.Player, NUM_ROUNDS):
        self.player1 = PLAYER1
        self.player2 = PLAYER2
        self.p1Gold = 0
        self.p2Gold = 0
        self.rounds = NUM_ROUNDS


    def run(self):



        for i in range(self.rounds):

            print(f"\n ROUND {i+1}")

            self.p1Gold += Play(self.player1).run()

            self.p2Gold += Play(self.player2).run()

        if self.p1Gold > self.p2Gold:
            print(f"\n {self.player1.getPlayerName()} has won with a TOTAL of {self.p1Gold} gold!")

        if self.p1Gold < self.p2Gold:
            print(f"\n {self.player2.getPlayerName()} has won with a TOTAL of {self.p2Gold} gold!")

        if self.p1Gold == self.p2Gold:
            print("\nNo one won this round :(")



class SinglePlayer:
    """
    Gamemode for the user to play the computer
    """

    def __init__(self, PLAYER:player.Player):
        self.player = PLAYER
        self.computer = Player("Computer")

    def run(self):

        PLAYER_GOLD = Play(self.player).run()
        COMPUTER_GOLD = Play(self.computer).computer()

        if PLAYER_GOLD > COMPUTER_GOLD:
            print(f"{self.player1.getPlayerName()} has won!")

        if PLAYER_GOLD < COMPUTER_GOLD:
            print(f"Computer has won!")

        else:
            print("No one won this round :(") # If there is a tie, their is no winner


class Game:
    """
    Game Engine Class
    """
    def __init__(self):
        pass

    def run(self):

        while True:

            ## -- INPUTS -- ##


            print("""\n \n
            -----------------------------------------------------------------------------------------------
            Welcome to the Game please select the game mode you want to play:
            
                1. Classic Game (2 Players; 1 Round)
                2. Best-Of Rounds (Play multiple rounds and the player who scores the most in total wins)
                3. Exit
                
            -----------------------------------------------------------------------------------------------
            """)

            INPUT = input("> ")

            INPUT = getInput(INPUT)


            ## -- PROCESSING + OUTPUTS -- ##

            if INPUT == 1:

                PLAYERS = []
                INDEX = []

                for i in range(2):
                    NAME = input(f"What is Player {i + 1}'s Name?: ")
                    PLAYERS.append(Player(NAME))

                for i in range(2):
                    RUN = Play(PLAYERS[i]).run()
                    INDEX.append(RUN)

                MAXIMUM = INDEX.index((max(INDEX))) # Gets the index of the Player with the highest roll

                if len(set(INDEX)) == 1: # if every player gets a 0, there is no winner.
                    print("\nNo One Won this Round :(")

                else:

                    print(f"\n{PLAYERS[MAXIMUM].getPlayerName()} has won!")


            # Best-of Rounds
            if INPUT == 2:
                PLAYERS = []
                ROUNDS = int(input("How many 'best-of' rounds would you like to play?: "))
                for i in range(2):
                    NAME = input(f"What is Player {i + 1}'s Name?: ")
                    PLAYERS.append(Player(NAME))
                bestOfThree(PLAYERS[0], PLAYERS[1], ROUNDS).run()

            if INPUT == 3:
                print("Thanks for playing!")
                exit()


def getInput(INPUT):
    """
    Error checks the input value entered
    :return: int
    """


    if INPUT == "1" or INPUT == "2" or INPUT == "3":
        return int(INPUT)
    else:
        print("Enter a choice from the menu!")
        NEW_INPUT = input("> ")
        getInput(NEW_INPUT)



if __name__ == "__main__":

    # The User only needs to run this to run the program.
    GAME = Game()
    GAME.run()





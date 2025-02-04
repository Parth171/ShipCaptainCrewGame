"""
title: Player Class
author: Parth Sakpal
date-created: 11/30/2023
"""

# Imports the Dice Class
from dice import Dice


class Player:

    def __init__(self, NAME):
        self.__playerName = NAME

        self.playerDices = [] # Contains all the player Dices

        self.activeDices = [] # Contains the active playing Dices of the user

        self.playerGold = 0


    def createDices(self, NUM):
        self.playerDices = []
        for i in range(NUM):
            self.playerDices.append(Dice())

    def getPlayerName(self):
        return self.__playerName

    def rollActiveDices(self):

        self.activeDices = []



        for i in range(len(self.playerDices)):
            self.activeDices.append(0)
            self.activeDices[i] = self.playerDices[i].rollDie()

        return self.activeDices


    def __str__(self):
        return self.__playerName


if __name__ == "__main__":

    ###### EVERYTHING BELOW IS FROM ME TESTING THIS CLASS #####

    DATA = [Dice(), Dice(), Dice()]

    Parth = Player("Parth")

    Parth.createDices(5)


    for i in range(3):
        Parth.rollActiveDices()








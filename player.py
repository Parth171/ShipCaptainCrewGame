"""
title: Player Class
author: Parth Sakpal
date-created: 11/30/2023
"""

from dice import *
from dice import Dice

class Player:

    def __init__(self, NAME):
        self.__playerName = NAME
        self.__playerDices = [Dice()]


    def rollDie(self):

        for i in range(len(self.__playerDices)):
            self.__playerDices[i] = self.__playerDices[i].rollDie()

        return self.__playerDices

    def removeDie(self, i):
        self.__playerDices[i].pop()


if __name__ == "__main__":
    PLAYER1 = Player("Parth")
    PLAYER1.rollDie()


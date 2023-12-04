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
        self.__playerDices = []
        self.__idleDices = []


    def returnName(self):
        return self.__playerName

    def createDies(self):
        for i in range(5):
            self.__playerDices.append(Dice())

    def getActiceDices(self):
        return self.__playerDices


    def rollActiveDies(self):

        for i in range(len(self.__playerDices)):
            self.__playerDices[i] = self.__playerDices.rollDie()

        return self.__playerDices

    def removeDie(self, i):
        self.__idleDices.append(self.__playerDices[i])
        self.__playerDices.pop(i)


if __name__ == "__main__":

    PLAYER = Player("Parth")

    PLAYER.createDies()

    PLAYER.rollActiveDies()

    print(PLAYER.getActiceDices())











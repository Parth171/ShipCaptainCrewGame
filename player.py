"""
title: Player Class
author: Parth Sakpal
date-created: 11/30/2023
"""


from dice import Dice # import this


class Player:

    def __init__(self, NAME):
        self.__playerName = NAME
        self.playerDices = []

        self.idleDices = []

        self.playerGold = 0

        ######


    def createDices(self, NUM):
        for i in range(NUM):
            self.playerDices.append(Dice())

    def getPlayerName(self):
        return self.__playerName

    def rollActiveDices(self):

        for i in range(len(self.playerDices)):
            self.playerDices[i].rollDie()

    def getRoll(self):

        for i in range(len(self.playerDices)):
            self.playerDices[i] = self.playerDices[i].getDieNumber()

        return self.playerDices





if __name__ == "__main__":

    PLAYER = Player("Parth")

    PLAYER.createDices(2)

    PLAYER.rollActiveDices()

    print(PLAYER.getRoll())








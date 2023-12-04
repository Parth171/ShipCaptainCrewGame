"""
title: Dice Class
author: Parth Sakpal
date-created: 11/30/2023
"""

from random import randint

class Dice:

    def __init__(self):
        self.__DiceNumber = 0


    def __str__(self):
        return self.__DiceNumber


    def rollDie(self):
        self.__DiceNumber = randint(1, 6)
        return self.__DiceNumber


if __name__ == "__main__":
    DICE = Dice()






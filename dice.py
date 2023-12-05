"""
title: Dice Class
author: Parth Sakpal
date-created: 11/30/2023
"""

from random import randint

class Dice:

    def __init__(self):
        self.DiceNumber = 0


    def __str__(self):
        return self.DiceNumber




    def rollDie(self):
        self.DiceNumber = randint(1, 6)

    def getDieNumber(self):
        return self.DiceNumber


if __name__ == "__main__":
    DICE = Dice()

    DICES = [Dice(), Dice(), Dice()] # works

    for i in range(len(DICES)):
        DICES[i].rollDie()










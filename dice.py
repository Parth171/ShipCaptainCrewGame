"""
title: Dice Class
author: Parth Sakpal
date-created: 11/30/2023
"""

# Imports the Random Library
from random import randint

class Dice:

    def __init__(self):
        self.DiceNumber = 0

    def rollDie(self):
        self.DiceNumber = randint(1,6)
        return self.DiceNumber



    def __str__(self):
        return self.DiceNumber




if __name__ == "__main__":
    DICE = Dice()

    DICES = [Dice(), Dice(), Dice()] # it works

    for i in range(len(DICES)):
        DICES[i].rollDie()










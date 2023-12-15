# CSE3120-Project

Ship, Captain, Crew Program

## Description 

This project features the popular dice game Ship, Captain, Crew! This version of the game features different game modes which the user an play to gain a fulfilled playing experience. 

## Dependancies
This project ultilizes the *random* library, which is in-built into Python. For this program, the user is not required to install any external libraries/external dependancies.

## Instructions

This program contains three files. The user is only requied to interact with the game.py file. Depending on the input option the user chooses from the menu, the user will be promted to input the name of the players playing in that current round.  Throughtout the program the user will be required to press ENTER to proceed with the program. This is done to embellish the user experience and ensure user engagement. 


## Extra Features

### Extra Feature 1. 
The requirements for the program state that their should be two players. In the normal game mode, the user has an option to choose between 2-5 players, like the traditional game allows. Each player object is stored in an array. The program chooses the player with the highest roll out of ALL the other players to determine the winner. 

### Extra Feature 2
I added a game mode where two users can play "Best of Three". In this game mode, two users go agaisnt one another three times and the program display the winner according on who got the highest gold throughout all three rounds played. In this feature, the game kept track of each player's gold using an array and summed the gold from each round to determine the winner. 

### Extra Feature 3
In this feature, the user has the option play against the computer, playing single player. This was to allow the user to play even when they are by themselves and don't have another play to play with them. In the game mode, the user still has to interact to roll their own dices, but the computer automates the rolling process, and the computer makes the desision of whether it wants to re roll for gold or not by itself. The computer logic is similar to the player logic, but changes have been made to ensure that the playing against the computer feels authentic and professional. 


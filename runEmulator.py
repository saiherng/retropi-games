
"""
Author : Sai Herng
Date   : 3/18/2018
"""

import os
import sys
import subprocess

def availableGames():
    userConsoleChoice = input("Select gba OR n64 OR snes : ")

    rootDir = os.getcwd()


    if userConsoleChoice == "gba":
        path = rootDir + r"\Games\Game Boy Advance Games"
        gamesDir = os.listdir(path)

        choiceDict = {}
        counter = 1

        for file in gamesDir:
            if file.endswith(".gba"):
               choiceDict[counter] = file
               counter += 1

    elif userConsoleChoice == "n64":
        path = rootDir + r"\Games\Nintendo 64 Games"
        gamesDir = os.listdir(path)

        choiceDict = {}
        counter = 1

        for file in gamesDir:
            if file.endswith(".z64"):
               choiceDict[counter] = file
               counter += 1

    elif userConsoleChoice == "snes":
        path = rootDir + r"\Games\Super Nintendo Games"
        gamesDir = os.listdir(path)

        choiceDict = {}
        counter = 1

        for file in gamesDir:
            if file.endswith(".smc"):
               choiceDict[counter] = file
               counter += 1

    return choiceDict,path


def openGame(game,path):
     for key in game:
           print(key, "--" , game[key])

     gameChoice = input("Enter game number: ")
     os.startfile(path + "\\" + game[int(gameChoice)])


def main():

        game, path = availableGames()
        openGame(game,path)



main()

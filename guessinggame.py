#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 21:45:50 2023

Code for the number guessing game.

@author: AmberC
"""

from random import randint

TotalPoints = 0

def GenerateGuess():
    return (randint(1, 10))

def CheckGuess(a,b):
    global TotalPoints
    
    if (a == b):
        TotalPoints =+ 5
        return True 
    else:
        return False

def main():
    global TotalPoints
    
    UserGuess     = 0
    ComputerGuess = 0 
    result        = 0
    
    UserGuess     = int(input("Let's play the Number Guessing Game \nMake a guess between 1 and 10: "))
    ComputerGuess = GenerateGuess()    
    result = CheckGuess(UserGuess, ComputerGuess)
    
    if (result == True):
        print("Congrats your total points are", TotalPoints)
    else:
        print("You Lose!")
    
    PlayAgain     = input("Would you like to play again? ")
    
    if (PlayAgain == "yes"):
        main()
    else: 
        print("Goodbye, your total ending points are", TotalPoints)
    
main()

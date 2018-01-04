# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 14:22:47 2018

@author: Twox3

"""

#0 — rock
#1 — Spock
#2 — paper
#3 — lizard
#4 — scissors

import random

def name_to_number(name) :
    if(name=="rock"):
        return 0
    elif(name=="spock"):
        return 1
    elif(name=="paper"):
        return 2
    elif(name=="lizard"):
        return 3
    elif(name=="scissors"):
        return 4
    else:
        return -1
    
    
def number_to_name(number):
    if(number==0):
        return "rock"
    elif(number==1):
        return "spock"
    elif(number==2):
        return "paper"
    elif(number==3):
        return "lizard"
    elif(number==4):
        return "scissors"
    else:
        return "Invalid number"
    
def rpsls(player_choice):
    player_choice_number=name_to_number(player_choice)
    computer_choice_number=random.randrange(0,4)
    
    #result = (PLayerChoice - Computer Choice modulo 5)
    #if result = 1 or 2 --- Player wins
    #else if result = 3 or 4-- Computer wins
    #else -- It is a tie
    print("Player Chooses "+player_choice)
    print("Computer Chooses "+number_to_name(computer_choice_number))
    result = (player_choice_number - computer_choice_number)%5
    
    if(result==1 or result == 2):
        print("Player Wins!!")
    elif(result==3 or result==4):
        print("Computer Wins!!")
    else:
        print("Player and computer tie!")
    
    print()
    return 0

rpsls("spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
rpsls("rock")

        
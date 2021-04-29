# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 05:43:45 2021

@author: Uday Sharma
"""

import random
print("Winning Rule  Od The Color Choice Game As Follows" + "\n Inter A Number One To Five And Computer Choice To Win The Computer")
computer_score = 0
player_score = 0
while True:
    print("Red = 1 \n Yellow = 2 \n Orange = 3 \n Green = 4 \n Blue = 5 \n Take A Turn")
    player_choice = int(input("User Turn:"))
    while player_choice >5 and player_choice <1:
          player_choice  = int(input("Enter Valid Input"))
    if player_choice == 1:
        choice_col = "Red"
    elif player_choice == 2:
        choice_col = "Yellow"
    elif player_choice == 3:
        choice_col = "Orange"
    elif player_choice == 4:
        choice_col = "Green"
    else:
        choice_col = "Blue"
    print("User Color Choice Is :" + choice_col)
    print("\n Now Its Compute Turn To Choose A Color")
    computer_choice = random.randint(1,5)
    while computer_choice  == player_choice:
          computer_choice  = random.randint(1,5)
    if player_choice ==1:
        compu_choice_col = "Red"
    elif player_choice ==2:
        compu_choice_col = "Yellow"
    elif player_choice ==3:
        compu_choice_col = "Orange"
    elif player_choice ==4:
        compu_choice_col = "Green"
    else:
        compu_choice_col = "Blue"
    print("Computer Color Choice Is" , compu_choice_col)
    if choice_col == compu_choice_col:
        player_score += 1
        print("Player_Score" + str(player_score))
        print("Computer_Score" + str(computer_score))
    else :
        computer_score += 1
        print("Player_Score" + str(player_score))
        print("Computer_Score" + str(computer_score))
    print("Do You Want To Play Again(Yes/No)")
    answer = input()
        
    if answer == "n" or answer == "N":
        break


if computer_score == player_score:
    print("Game Is Tied")
    print("\n Thank For Playing")
elif computer_score < player_score:
    print("Player Is Victorious")
    print("< == User Wins == >")
    print("\n Thank For Playing")
elif computer_score > player_score:
    print("\n <== Computer Win ==>")
    print("\n Player Is Defeated")
    print("\n Thank For Playing")

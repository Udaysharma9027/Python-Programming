# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 22:05:07 2021

@author: Uday Sharma
"""

{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "Part #1\n",
    "- Create a board for tic tac toe that looks something like this:\n",
    "\n",
    "x| |\n",
    " |o|\n",
    " | |x     (hint: you can use '\\n' to print on a new line)   TICK=============================\n",
    " \n",
    " - User can enter a space between 1-9 and an x will appear in that spot TICK ===============\n",
    " - User can then do the same and an o will appear TICK ====================\n",
    " ================================================\n",
    " Part #2\n",
    " - If user tries to enter a space that is already taken, they are not allowed and have to try again TICK =================\n",
    " - If user gets three in a row, game ends and the winner is announced  TICK ==========================\n",
    "=================================================\n",
    " Part #3\n",
    " - User can choose whether to play with a friend (using the same keyboard) or against the computer TICK ===========\n",
    " - Design the computer to make its own moves TICK =========================================\n",
    "'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "board = [\" \"] * 9"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "def draw_board(board):\n",
    "    row_1 = \"{}|{}|{}\".format(board[0],board[1],board[2])\n",
    "    row_2 = \"{}|{}|{}\".format(board[3],board[4],board[5])\n",
    "    row_3 = \"{}|{}|{}\".format(board[6],board[7],board[8])\n",
    "\n",
    "    print(row_1+'\\n'+row_2+'\\n'+row_3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "def user_move(board, user_type):\n",
    "    user_choice=int(input('Choose your space between 1-9')) - 1\n",
    "    if board[user_choice] != ' ':\n",
    "        print('Space is taken. Try again!')\n",
    "        user_move(board, user_type)\n",
    "    else:\n",
    "        board[user_choice]=user_type\n",
            available_spaces.remove(user_choice)\n
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "def comp_move(board, user_type):\n",
    "    computer_choice = random.choice(available_spaces)\n",
    "    board[computer_choice]=user_type\n",
    "    available_spaces.remove(computer_choice)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "def check_win(board, x_o):\n",
    "    if board[0] == x_o and board[1] == x_o and board[2] == x_o or board[3] == x_o and board[4] == x_o and board[5] == x_o or board[6] == x_o and board[7] == x_o and board[8] == x_o or board[0] == x_o and board[3] == x_o and board[6] == x_o or board[1] == x_o and board[4] == x_o and board[7] == x_o or board[2] == x_o and board[5] == x_o and board[8] == x_o or board[0] == x_o and board[4] == x_o and board[8] == x_o or board[2] == x_o and board[4] == x_o and board[6] == x_o:\n",
    "        play=False\n",
    "        print(\"Hooray! {} has won\".format(x_o))\n",
    "    else:\n",
    "        play=True\n",
    "    return play\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " | | \n",
      " | | \n",
      " | | \n",
      "Would you like to play against the computer or friend? (c or f)c\n",
      "Choose your space between 1-91\n",
      "x| | \n",
      " | | \n",
      " | | \n",
      "x| | \n",
      "o| | \n",
      " | | \n",
      "Choose your space between 1-92\n",
      "x|x| \n",
      "o| | \n",
      " | | \n",
      "x|x| \n",
      "o|o| \n",
      " | | \n",
      "Choose your space between 1-98\n",
      "x|x| \n",
      "o|o| \n",
      " |x| \n",
      "x|x| \n",
      "o|o| \n",
      " |x|o\n",
      "Choose your space between 1-97\n",
      "x|x| \n",
      "o|o| \n",
      "x|x|o\n",
      "x|x| \n",
      "o|o|o\n",
      "x|x|o\n",
      "End of the game\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "board = [\" \"] * 9\n",
    "available_spaces = [0,1,2,3,4,5,6,7,8]\n",
    "draw_board(board)\n",
    "play = True\n",
    "comp_or_friend = input(\"Would you like to play against the computer or friend? (c or f)\")\n",
    "while play==True:\n",
    "    \n",
    "    user_move(board,'x')\n",
    "    play=check_win(board,'x')\n",
    "    if play==False:\n",
    "        continue\n",
    "    draw_board(board)\n",
    "    if comp_or_friend == 'f':\n",
    "        user_move(board, 'o')\n",
    "    elif comp_or_friend == 'c':\n",
    "        comp_move(board, 'o')\n",
    "    play=check_win(board,'o')\n",
    "    draw_board(board)\n",
    "\n",
    "print('End of the game')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

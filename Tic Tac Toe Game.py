board = [""]*9
def draw_board(board):
    row_1 = "{}|{}|{}".format(board[0], board[1] , board[2])
    row_2 = "{}|{}|{}".format(board[3], board[4] , board[5])
    row_3 = "{}|{}|{}".format(board[6], board[7] , board[8])
    print(row_1+'\\n'+row_2+'\\n'+row_3)
def user_move(board , user_type):
    user_choice = int(input("Choose your space between 1-9"))-1
if board[user_choice]!="":
    print("Space is taken . Try Again!")
    user_move(board , user_type)
else:
    board[user_choice] = user_type
    available_space.remove(user_choice)
def comp_move(board , user_type):
    computer_choice = random.choice(available_space)
    board[computer_choice] = user_type
    available_space.remove(computer_choice)
def check_win(board , x_o):
    
      if board[0]==x_o and board[1]==x_o and board[2]==x_o or board[3]==x_o and board[4]==x_o and board[5]==x_o or board[6]==x_o and board[7]==x_o and board[8]==x_o or board[0]==x_o and board[3]==x_o and board[6]==x_o or board[1]==x_o and board[4]==x_o and board[7]==x_o or board[2]==x_o and board[5]==x_o and board[8]==x_o or board[0]==x_o and board[4]==x_o and board[8]==x_o or board[2]==x_o and board[4]==x_o and board[6]==x_o:
          play = False
          print("Hooray:{} has been".format(x_o))
      else:
          
         play = True
         return play
     
      import random
      board[""]*9
      available_space = [0, 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8]
      draw_board(board)
      play = True
      computer_or_friend = input("Would you like to play against the computer or friend ? (computer and friend)")     
      while play ==True:
          user_move(board , "x")
          play =  check_win(board , "x")
      if play == False:
          continue
      draw_board(board)
      if computer_or_friend == "F":
        user_move(board , "o")
      elif computer_or_friend == "c":
        comp_move(board , "o")
        play = check_win(board , "o")
        draw_board(board)
print("End of the program")
          
      
      
         
     
          
         
     
        
     
     
        
    
    
            
        
    

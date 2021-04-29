# Number Guessing Challenge

import random
computer_num = random.randint(1, 100)
user_guess = int(input("Please enter a number between 1 to 100"))
print("your guess: {} , the actural compuer number :{}".format(user_guess , computer_num))

if user_guess == computer_num:
    print("congratulation ! your guess was currect")
elif user_guess > computer_num :
    print("Too High")
elif user_guess < computer_num :
    print ("Too Low")
else:
    print("ohh! bad news this is wrong ")
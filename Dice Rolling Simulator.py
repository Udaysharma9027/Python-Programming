# Dice Rolling Simulator Program

from random import randint

num_one = randint(1, 6)

num_two = randint(1, 6)

dice_total = num_one + num_two

print("Dice simulation complete! numOne {} and numTwo {} . The resut is {}".format(num_one , num_two , dice_total))

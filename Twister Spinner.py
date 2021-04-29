# Twister Spinner

import random

colors = ["Red" , "Black" , "Blue" , "Yellow"]
body_part = ["Left foot" , "Right foot" , "Left hand" , "Right Hand"]

color_choice = random.choice(colors)
body_choice = random.choice(body_part)
print("Twister Spinner say : {} {}".format(body_choice , color_choice))
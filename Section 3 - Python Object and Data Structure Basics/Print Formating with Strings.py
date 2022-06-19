from termcolor import cprint, colored
from datetime import date

# Print Formatting with Strings
#
# Formatting with the .format method
#
# Get user's name and age
user_name = input(">>> Enter your name here: \n")
user_age = input(">>> How old are you? \n")
# Prints user's info
print(">>> Hi, {}! You are {} years old--nice!".format(user_name, user_age))
#
cprint("The {2} {0} is {1}.".format("brown", "fox", "quick"), "yellow") # Will enter strings in the order supplied inside the curly braces.
#
# Float formatting follows "{value:width.precision f}"
result = 100 / 777
cprint("The result was {r:1.3f}".format(r=result), "white", "on_green")
#
# f-strings
name = "Jeremy"
age = 29
print(f"Hi, {name}! You are {age} years old.")
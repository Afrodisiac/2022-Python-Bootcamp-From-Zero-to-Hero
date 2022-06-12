from termcolor import colored, cprint

# Intro to Strings - Notes
#
# Strings are ORDERED sequences; can use indexing and slicing
# to grab sub-sections of code.
#
# Indexing notation uses [], which allows you to grab a single
# character from the string.
#
# Indexing starts at zero. For instance, if you wanted to grab
# the character "B" from the string below, you would use index [4].
my_string = "goodbye"
cprint(f"The character at index [4]  of the {my_string} is {my_string[4]}.", "green",)
#
# If you wanted to grab the last letter of a string, but did not
# know the length of the string. One option is to use the reverse
# index function, as shown below.
my_new_string = "hallelujah"
cprint(f"The last character in {my_new_string} is {my_new_string[-1]}.", "magenta")
#
# Slicing allows you to grab a sub-section or "slice" of a string;
# follows [start:stop:step] syntax, as shown below.
#
# * Hint: START is the numerical index for the slice start, STOP is the
# index you will go up to (but not include), and STEP is the size of the "jump".
#
cprint(f"The string {my_new_string} says {my_new_string[:2]} using a [:2] slice.", "red")
#
# Another example would be to "jump" a certain amount of times:
alpha_string = "abcdefghijklmnopqrstuvwxyz"
cprint(f"This is the alphabet, with a step of 2: {alpha_string[::2]}", "yellow")
#
# Another neat trick is to use reverse indexing to reverse a string:
cprint(f"Here is the alphabet reversed: {alpha_string[::-1]}", "grey")

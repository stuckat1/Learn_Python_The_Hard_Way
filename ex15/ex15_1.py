# bring in argv into program
from sys import argv

# unpack script name and user provided input
script, filename = argv

# get handle to file
txt = open(filename)

# echo file name
print "Here's your file %r:" % filename

# slurp contents and echo
print txt.read()

# reprompt users
print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

# slurp and echo
print txt_again.read()
# Print one variable using format
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"

# Print two variables using two formats
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y


# Print one variable using one format
print "I said: %r." % x

# Print one variable using one format
print "I also said: '%s'." % y

hilarious = False
# Print boolean as catch-all format
joke_evaluation = "Isn't that joke so funny?! %r"

# Print one variable using one format
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

# Print two strings by concatenation
print w + e
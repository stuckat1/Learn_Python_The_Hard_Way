def loop( x, y ) :

    i = 0

    while i < x:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + y
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i



numbers = []

loop(4,2)

print "The numbers: "

for num in numbers:
    print num


# reset
numbers[:] = []

loop(6,3)

print "The numbers: "

for num in numbers:
    print num
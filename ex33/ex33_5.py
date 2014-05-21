def loop( x) :


    for i in range(x) :

        print "At the top i is %d" % i
        numbers.append(i)

        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i



numbers = []

loop(4)

print "The numbers: "

for num in numbers:
    print num


# reset
numbers[:] = []

loop(6)

print "The numbers: "

for num in numbers:
    print num
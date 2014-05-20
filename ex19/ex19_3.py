def myfun( x, y) :

    return x ** 2 + y

for i in range(5) :
    for j in range(5) :
        print "myfun(%d, %d) => %d" % (i,j,myfun(i,j))


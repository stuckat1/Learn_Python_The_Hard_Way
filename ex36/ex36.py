# Circular arrangement of rooms

from sys import exit


def room_b( prev_room ) :

    print "This is an empty room.  There is a single door ahead and behind you."
    print "Which door do you take?"

    choice = raw_input('>')

    if prev_room == "start" :

        if choice == "ahead" :
            room_a("b")
        elif choice == "behind" :
            start()
        else :
            print "Your dead!"
            exit

    elif prev_room == "a" :

        if choice == "ahead" :
            start()
        elif choice == "behind" :
            room_a("b")
        else :
            print "Your dead!"
            exit

    else :
        print "Your dead!"
        exit

def room_a( prev_room ) :

    print "This is an empty room.  There is a single door ahead and behind you."
    print "Which door do you take?"

    choice = raw_input('>')

    if prev_room == "start" :

        if choice == "ahead" :
            room_b("a")
        elif choice == "behind" :
            start()
        else :
            print "Your dead!"
            exit

    elif prev_room == "b" :

        if choice == "ahead" :
            start()
        elif choice == "behind" :
            room_b("a")
        else :
            print "Your dead!"
            exit

    else :
        print "Your dead!"
        exit


def start() :

    print "There are two doors, left and right."
    print "Which door do you take?"

    choice = raw_input('>')

    if choice == "left" :
        room_a("start")
    elif choice == "right" :
        room_b("start")
    else :
        print "Your dead!"
        exit

start()

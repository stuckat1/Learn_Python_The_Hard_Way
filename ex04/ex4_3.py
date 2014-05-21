# number of cars
cars = 100

# seats in car
space_in_a_car = 4.0

# number of people who want to drive
drivers = 30

# people who can't or won't drive or don't care ... if they are in Detroit
passengers = 90

# number of cars without drivers
cars_not_driven = cars - drivers

# assume all drivers drive ... surplise
cars_driven = drivers

# total number of people that can be transported
carpool_capacity = cars_driven * space_in_a_car

# average passengers for cars driven.  
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
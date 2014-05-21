# create a mapping of state to abbreviation
states = {
    'Maine': 'ME',
    'Vermont': 'VT',
    'Massachusetts': 'MA',
    'Connecticut': 'CT',
    'Rhode Island': 'RI'
}

# create a basic set of states and some cities in them
cities = {
    'ME': 'Augusta',
    'VT': 'Montpelier',
    'MA': 'Massachusetts'
}

# add some more cities
cities['CT'] = 'Hartford'
cities['RI'] = 'Providence'

# print out some cities
print '-' * 10
print "CT State has: ", cities['CT']
print "RI State has: ", cities['RI']

# print some states
print '-' * 10
print "Connecticut's abbreviation is: ", states['Connecticut']
print "Vermont's abbreviation is: ", states['Vermont']

# do it by using the state then cities dict
print '-' * 10
print "Connecticut has: ", cities[states['Connecticut']]
print "Vermont has: ", cities[states['Vermont']]

# print every state abbreviation
print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)

# print every city in state
print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

# now do both at the same time
print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (
        state, abbrev, cities[abbrev])

print '-' * 10
# safely get a abbreviation by state that might not be there
state = states.get('New York', None)

if not state:
    print "Sorry, no New York."

# get a city with a default value
city = cities.get('NY', 'Does Not Exist')
print "The city for the state 'NY' is: %s" % city
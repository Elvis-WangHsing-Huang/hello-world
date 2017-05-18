# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print '-'*10
print "NY State has:", cities['NY']
print "OR State has:", cities['OR']

# print some states
print '-'*10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# do it by using the states then cities dict
print '-'*10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# print every state abbreviation
print '-'*10
for st, ab in states.items():
    print "%s state is abbrivated as %s" %( st, ab)

# print every city in state
print '-' * 10
for ab, ct in cities.items():
    print "%s has the city %s" %(ab, ct)

# now, do both at the same time
print '-' * 10
for st, ab in states.items():
    print "%s state is abbrivated as %s has city: %s" %(st, ab, cities[ab])

print '-' * 10
# safely get an abbreviation by state that might not be there
# dict.get(key) is a safer way for handling exception
# than dict[key]
state = states.get('Texas')
# state = NONE
if not state:
    print "Sorry, no Texas."

# get a city with a default value
city = cities.get("TX", 'Does Not Exist!')
print "The city for the state 'TX'is: %s" %(city)

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count:
    print "This is count %d" % number

for fruit in fruits:
    print "A fruit of type: %s" % fruit

# change is a mixed lists, we have to use %r since we don't know what is in it
for i in change:
    print "I got %r" % i
# we can also build lists

elements = [] # a list with no element

for i in range(0,6):
    print "Adding %d to the list" % i
    elements.append(i)
print elements

for i in elements:
    print "Element was: %d" % i
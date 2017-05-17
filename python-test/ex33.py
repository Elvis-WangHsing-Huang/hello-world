# i = 0
numbers = []

"""
while i < 6 :
    print "At the top i is %d" % i
    numbers.append(i)
    
    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i
"""

def append_list (upper, nums):
    i = 0
    while i < upper:
        print "At the top i %d" % i
        nums.append(i)
        i = i +1
        print "Nums now: ", nums
        print "At the bottom i is %d" %i

append_list(8, numbers)
print "The  numbers: "

for num in numbers:
    print num

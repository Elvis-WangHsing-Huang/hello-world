from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit Ctrl-C (^C)."
print "If you do want that, hit RETURN"

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncate the file. Goodbye!"
target.truncate();

print "Now, I am going to ask you for three lines."

line1 = raw_input("line1:")
line2 = raw_input("line2:")
line3 = raw_input("line3:")

print "I am going to write these to the file"

"""
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
"""
target.write("%s\n%s\n%s\n" %(line1, line2, line3))
print "And finally, we close it."
target.close()

target = open(filename)
print "The new file shows:"
print(target.read())
target.close()

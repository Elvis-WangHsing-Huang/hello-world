# get the argv feature (module) from the sys package
from sys import argv

# collect the script_name, first parameter from the argv list
script, filename = argv

text = open(filename)

print "Here is your file %r:" % filename
print text.read()
text.close()

print "Type the filename again:"
file_again = raw_input("> ")

text_again = open(file_again)
print text_again.read()
text_again.close()

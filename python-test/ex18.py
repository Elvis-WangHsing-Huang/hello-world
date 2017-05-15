def print_more(*args):
    #arg1, arg2 = args
    #print "arg1: %r, arg2: %r" %(arg1, arg2)
    for arg in args:
        print "%r" %arg
print_more("Elvis", "Alice","Bryan","Amanda")

def print_two(arg1, arg2):
    print "arg1:%r, arg2:%r" %(arg1, arg2)
print_two("Amanda", "Bryan")

def print_one(arg1):
    print "arg1: %r" %arg1

print_one("Elvis")

def print_none():
    print "I got noothin'."

print_none()

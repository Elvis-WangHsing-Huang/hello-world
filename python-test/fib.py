# use of the yield => to convert a function to become a generator
# see https://puremonkey2010.blogspot.tw/2016/05/python-python-yield.html


def fib(N):
    n,a,b = 0,0,1
    while n < N :
        print b
        a, b = b, a+b
        n = n+1


def fib2(N):
    n,a,b = 0,0,1
    L = [] # return list => it will use more storage
    while n < N :
        L.append(b)
        a, b = b, a+b
        n = n+1
    return L

def  fib3(N):
    n,a,b = 0,0,1
    while n < N :
        yield b # this will cause fib3 to become a generator,
                #  which will be called in the iterator
        a, b = b, a+b
        n = n+1


print("use fib(10)")
fib(10)

print("use fib2(10)")
for i in fib2(10):
    print i

print("use fib3(10)")
for i in fib3(10):
    print i

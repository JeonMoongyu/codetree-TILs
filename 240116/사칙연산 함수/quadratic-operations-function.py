def add(a,b):
    return a+b


def subt(a,b):
    return a-b


def mult(a,b):
    return a*b


def div(a,b):
    return a//b


a,o,c = input().split()
a,c = int(a), int(c)

if o == "+":
    print(a,o,c,"=",add(a,c))
elif o == "-":
    print(a,o,c,"=",subt(a,c))
elif o == "*":
    print(a,o,c,"=",mult(a,c))
elif o == "/":
    print(a,o,c,"=",div(a,c))
else:
    print(False)
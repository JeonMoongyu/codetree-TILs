binary = list(map(int,list(input())))
num = 0
for digit in binary:
    num = num*2 + digit
print(num)
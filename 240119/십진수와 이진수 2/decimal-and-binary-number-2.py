b = list(map(int,list(input())))

n = 0
for digit in b:
    n = n*2 + digit

n *= 17

arr = []
while True:
    if n < 2:
        arr.append(n)
        break
    arr.append(n%2)
    n //= 2

for digit in arr[::-1]:
    print(digit, end="")
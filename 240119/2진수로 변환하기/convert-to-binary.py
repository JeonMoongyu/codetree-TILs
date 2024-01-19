n = int(input())
digits = []

while n:
    digits.append(n%2)
    n //= 2

for digit in digits[::-1]:
    print(digit, end="")
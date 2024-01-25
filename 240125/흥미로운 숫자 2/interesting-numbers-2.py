x,y = tuple(map(int,input().split()))


def is_interesting(n):
    num_of_digits = [0] * 10
    while n > 0:
        num_of_digits[n%10] += 1
        n //= 10
    a, b = 0, 0
    for d in range(10):
        if num_of_digits[d] == 1:
            a += 1
        if num_of_digits[d] > 1:
            b += 1
    return a == 1 and b == 1


ans = 0
for n in range(x,y+1):
    if is_interesting(n):
        ans += 1

print(ans)
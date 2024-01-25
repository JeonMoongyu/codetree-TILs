x,y = tuple(map(int,input().split()))


def sum_of_digits(z):
    if z < 10:
        return z
    return z%10 + sum_of_digits(z//10)


ans = 0
for num in range(x,y+1):
    ans = max(ans,sum_of_digits(num))
print(ans)
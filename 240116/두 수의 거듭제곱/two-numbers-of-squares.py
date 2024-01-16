def exp_ft(a,b):
    result = 1
    for _ in range(b):
        result *= a
    return result

a,b = tuple(map(int,input().split()))
print(exp_ft(a,b))
def is_prime(n):
    if n==1:
        return False
    satisfied = True
    for i in range(2,n):
        if n%i==0:
            satisfied = False
    return satisfied


def sum_of_jaritsoo(n):
    sum_val = 0
    while n > 0:
        sum_val += n%10
        n //= 10
    return sum_val


def is_wanted_num(n):
    return is_prime(n) and sum_of_jaritsoo(n)%2==0


a,b = tuple(map(int,input().split()))
cnt = 0
for i in range(a,b+1):
    if is_wanted_num(i):
        cnt += 1
print(cnt)
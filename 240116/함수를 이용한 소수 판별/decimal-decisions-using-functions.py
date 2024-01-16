def is_prime(n):
    if n==1:
        return False
    for i in range(2,n//2):
        if n%i==0:
            return False
    return True


a,b = tuple(map(int,input().split()))
sum_val = 0
for n in range(a,b+1):
    if is_prime(n):
        sum_val += n

print(sum_val)
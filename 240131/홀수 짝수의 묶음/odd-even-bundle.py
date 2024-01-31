n = int(input())
arr = list(map(int,input().split()))

even = 0
for elem in arr:
    if elem % 2 == 0:
        even += 1
odd = n - even


while odd > even:
    odd -= 2
    even += 1

if even > odd:
    print(2*odd+1)
else: # even == odd
    print(2*odd)
a,b = tuple(map(int,input().split()))
n = int(input())


ten = 0
for digit in str(n):
    ten = ten*a + int(digit)
    
arr=[]
while True:
    if ten<b:
        arr.append(ten)
        break
    arr.append(ten%b)
    ten //= b

for digit in arr[::-1]:
    print(digit, end="")
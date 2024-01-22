def not_carry(a,b,c):
    if a < 10 and b < 10 and c < 10:
        return a+b+c < 10
    return (a%10)+(b%10)+(c%10) < 10 and not_carry(a//10,b//10,c//10)


n = int(input())
arr = [
    int(input())
    for _ in range(n)
]
max_sum = -1
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if not_carry(arr[i],arr[j],arr[k]):
                max_sum = max(max_sum,arr[i]+arr[j]+arr[k])
print(max_sum)
n = int(input())
arr = list(map(int,input().split()))
arr1 = [ (i+1,arr[i]) for i in range(n) ]
arr1.sort(key= lambda x: x[1])

ans = -1
for i in range(1,n):
    if arr1[i][1] > arr1[0][1]:
        if i+1 < n and arr1[i+1][1] == arr1[i][1]:
            break
        ans = arr1[i][0]
        break
print(ans)
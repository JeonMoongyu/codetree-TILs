arr = list(map(int,input().split()))
arr.sort()
print(arr[0],arr[1],arr[2],arr[-1]-arr[0]-arr[1]-arr[2])
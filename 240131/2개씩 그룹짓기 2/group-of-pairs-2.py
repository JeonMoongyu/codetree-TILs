n = int(input())
arr = list(map(int,input().split()))
arr.sort()

differences = [ arr[n+i]-arr[i] for i in range(n) ]
print(min(differences))
import sys

n = int(input())
arr = list(map(int,input().split()))

# + + +
# + - -
# 

arr1 = sorted(arr)
ans1 = arr1[-1] * arr1[-2] * arr1[-3]   # + + +
ans2 = arr1[-1] * arr1[0] * arr1[1]     # + - -

if ans1 > 0 or ans2 > 0:
    print(max(ans1,ans2))
    sys.exit()

arr2 = sorted(arr, key= lambda x: abs(x))
print(arr2[0]*arr2[1]*arr2[2])
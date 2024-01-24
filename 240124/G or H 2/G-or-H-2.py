import sys

n = int(input())
places = [ 0 for _ in range(101) ]

for _ in range(n):
    pos, alp = input().split()
    pos = int(pos)
    num = 1 if alp == 'G' else -1
    places[pos] = num


def is_wanted_pic(arr):
    if arr[0] == 0 or arr[-1] == 0:
        return False
    if sum(arr) == 0:
        return True
    for elem in arr[1:]:
        if elem != arr[0]:
            return False
    return True


for k in range(100,-1,-1):
    for i in range(101-k):
        if is_wanted_pic(places[i:i+k+1]):
            print(k)
            sys.exit()
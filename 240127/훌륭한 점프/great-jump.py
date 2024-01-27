n,k = tuple(map(int,input().split()))
stones = list(map(int,input().split()))

def max_dist(arr, max_val):
    indices = [ i for i in range(len(arr)) if arr[i] <= max_val ]
    distances = [ indices[j+1]-indices[j] for j in range(len(indices)-1) ]
    return max(distances)

for a in range(n,0,-1):
    if max_dist(stones,a) > k:
        print(a+1)
        break
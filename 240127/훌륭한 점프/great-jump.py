n,k = tuple(map(int,input().split()))
stones = list(map(int,input().split()))


def max_dist(arr, max_val):
    indices = [ i for i in range(len(arr)) if arr[i] <= max_val ]
    distances = [ indices[j+1]-indices[j] for j in range(len(indices)-1) ]
    return max(distances)


ans = n
while ans > 1:
    if max_dist(stones, ans-1) > k:
        break
    ans -= 1
print(ans)
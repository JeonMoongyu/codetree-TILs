n,k = tuple(map(int,input().split()))
stones = list(map(int,input().split()))


def max_dist(arr, max_val):
    indices = [ i for i in range(len(arr)) if arr[i] <= max_val ]
    distances = [ indices[j+1]-indices[j] for j in range(len(indices)-1) ]
    return max(distances)


ans = max(stones[0], stones[-1])
while ans < 100:
    if max_dist(stones, ans+1) <= k:
        print(ans+1)
        break
    ans += 1
print(ans)
n,k = tuple(map(int,input().split()))
stones = list(map(int,input().split()))


def end_points_ok(arr, max_val):
    return arr[0] <= max_val and arr[-1] <= max_val

def max_dist(arr, max_val):
    indices = [ i for i in range(len(arr)) if arr[i] <= max_val ]
    distances = [ indices[j+1]-indices[j] for j in range(len(indices)-1) ]
    return max(distances)


ans = 100
while ans > 1:
    if not end_points_ok(stones, ans-1) or max_dist(stones, ans-1) > k:
        break
    ans -= 1
print(ans)
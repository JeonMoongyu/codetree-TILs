n = int(input())
seats = list(map(int,str(input())))


def min_dist(arr):
    result = 20
    for i in range(n):
        if arr[i] == 1:
            for j in range(i+1,n):
                if arr[j] == 1:
                    result = min(result,j-i)
    return result


ans = 0
for i in range(n):
    if seats[i] == 0:
        seats[i] = 1
        ans = max(ans,min_dist(seats))
        seats[i] = 0

print(ans)
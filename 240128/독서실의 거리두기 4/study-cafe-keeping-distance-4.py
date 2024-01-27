n = int(input())
seats = list(map(int,input()))


def dist(arr):
    indices = [ i for i in range(n) if arr[i]==1 ]
    distances = [ indices[j+1]-indices[j] for j in range(len(indices)-1) ]
    return min(distances)


ans = 1
for i in range(n):
    for j in range(i+1,n):
        if seats[i] == 1 or seats[j] == 1:
            continue
        temp = seats[:i] + [1] + seats[i+1:j] + [1] + seats[j+1:]
        ans = max(ans,dist(temp))
print(ans)
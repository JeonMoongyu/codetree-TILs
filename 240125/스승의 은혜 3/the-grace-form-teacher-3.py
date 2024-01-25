n,budget = tuple(map(int,input().split()))
arr = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

ans = 0
for i in range(n):
    arr_ith = [ arr[k] for k in range(n) ]
    arr_ith[i] = (arr[i][0]//2, arr[i][1])
    arr_ith.sort(key= lambda x: x[0]+x[1])

    cost, num_of_students = 0, 0
    for j in range(n):
        if cost + arr_ith[j][0] + arr_ith[j][1] > budget:
            break
        cost += arr_ith[j][0] + arr_ith[j][1]
        num_of_students += 1
    ans = max(ans,num_of_students)

print(ans)
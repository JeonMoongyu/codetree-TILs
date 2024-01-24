n = int(input())
questions = [
    tuple(map(int,input().split()))
    for _ in range(n)
]


def all_diff(i,j,k):
    return i!=j and i!=k and j!=k 


def count_1(i,j,k,num):
    n1 = num%10
    n2 = (num//10)%10
    n3 = num//100
    result = 0
    if i == n1:
        result += 1
    if j == n2:
        result += 1
    if k == n3:
        result += 1
    return result


def count_2(i,j,k,num):
    n1 = num%10
    n2 = (num//10)%10
    n3 = num//100
    result = 0
    if i == n2 or i == n3:
        result += 1
    if j == n1 or j == n3:
        result += 1
    if k == n1 or k == n2:
        result += 1
    return result


ans = 0
for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            if not all_diff(i,j,k):
                continue
            satisfied = True
            for num, cnt1, cnt2 in questions:
                if count_1(i,j,k,num) != cnt1 or count_2(i,j,k,num) != cnt2:
                    satisfied = False
                    break
            if satisfied:
                ans += 1

print(ans)
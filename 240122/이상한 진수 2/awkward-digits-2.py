a = list(map(int,list(input())))


def decimal(b_list):
    result = 0
    for j in range(len(b_list)):
        result = result*2 + b_list[j]
    return result


max_N = 0
for i in range(len(a)):
    a[i] = (a[i]+1)%2
    max_N = max(max_N, decimal(a))
    a[i] = (a[i]+1)%2

print(max_N)
a = list(map(int,list(input())))


def decimal(b_list):
    if len(b_list) == 1:
        return b_list[0]
    return decimal(b_list[:-1])*2 + b_list[-1]


max_N = 0
for i in range(len(a)):
    a[i] = (a[i]+1)%2
    max_N = max(max_N, decimal(a))
    a[i] = (a[i]+1)%2

print(max_N)
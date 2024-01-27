n = int(input())
arr = list(map(int,input().split()))


def is_perm(seq):
    for i in range(len(seq)):
        if seq[i] <= 0 or seq[i] > n:
            return False
    for i in range(len(seq)):
        for j in range(i+1,len(seq)):
            if seq[i] == seq[j]:
                return False
    return True


for a in range(1,n+1):
    seq = [a]
    for i in range(1,n):
        seq.append(arr[i-1]-seq[i-1])
    if is_perm(seq):
        for elem in seq:
            print(elem, end=" ")
        break
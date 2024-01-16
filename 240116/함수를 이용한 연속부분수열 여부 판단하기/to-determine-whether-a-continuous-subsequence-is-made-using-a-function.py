def is_cons_subseq(arr1, arr2):
    n,m = len(arr1), len(arr2)
    for i in range(n-m+1):
        if arr1[i] == arr2[0]:
            satisfied = True
            for j in range(m):
                if arr1[i+j] != arr2[j]:
                    satisfied = False
            if satisfied:
                return True
    return False

n,m = tuple(map(int,input().split()))
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

if is_cons_subseq(arr1, arr2):
    print("Yes")
else:
    print("No")
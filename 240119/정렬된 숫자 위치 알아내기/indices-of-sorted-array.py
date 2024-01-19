class Term:
    def __init__(self, value=0, index=0):
        self.value = value
        self.index = index

n = int(input())
arr = list(map(int,input().split()))
seq = [
    Term(arr[i],i+1)
    for i in range(n)
]

seq.sort(key = lambda x: (x.value, x.index))
ans = [0] * (n+1)
for i, term in enumerate(seq,start=1):
    ans[term.index] = i

for elem in ans[1:]:
    print(elem, end=" ")
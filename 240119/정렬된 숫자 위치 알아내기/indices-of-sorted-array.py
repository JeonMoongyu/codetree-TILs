class Term:
    def __init__(self, value=0, index=0, order=0):
        self.value = value
        self.index = index
        self.order = order

n = int(input())
arr = list(map(int,input().split()))
seq = [
    Term(arr[i],i+1,0)
    for i in range(n)
]

seq.sort(key = lambda x: (x.value, x.index))
for i in range(n):
    seq[i].order = i+1

seq.sort(key = lambda x: x.index)
for term in seq:
    print(term.order, end=" ")
import sys

n = int(input())
word = input()

for k in range(1,n+1):
    exist = False
    for i in range(n-k):
        for j in range(i+1,n-k+1):
            if word[i:i+k] == word[j:j+k]:
                exist = True
                break
        if exist:
            break
    if exist:
        continue
    print(k)
    sys.exit()
N,K,P,T = tuple(map(int,input().split()))

infested = [0 for _ in range(N+1)]
count = [0 for _ in range(N+1)]
infested[P] = 1
count[P] = K

handshake = [(0,0) for _ in range(251)]
for _ in range(T):
    t,x,y = tuple(map(int,input().split()))
    handshake[t] = (x,y)

for t,(x,y) in enumerate(handshake[1:],start=1):
    if infested[x] == 1 and infested[y] == 0:
        if count[x] > 0:
            infested[y] = 1
            count[y] = K
            count[x] -= 1
    elif infested[x] == 0 and infested[y] == 1:
        if count[y] > 0:
            infested[x] = 1
            count[x] = K
            count[y] -= 1
    elif infested[x] == 1 and infested[y] == 1:
        if count[x] > 0:
            count[x] -= 1
        if count[y] > 0:
            count[y] -= 1

for elem in infested[1:]:
    print(elem,end="")
x = int(input())


def max_dist(t):
    if t % 2 == 0:
        return (t+2)*t//4
    else:
        return (t+1)**2//4


for t in range(1,200):
    if max_dist(t) >= x:
        print(t)
        break
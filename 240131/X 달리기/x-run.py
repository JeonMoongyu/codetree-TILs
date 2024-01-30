x = int(input())

for t in range(1,200):
    vel = 1
    pos = 1
    for time in range(1,t):
        if vel - 1 == t - time:
            vel -= 1
        elif vel - 1 <= t - time - 2:
            vel += 1
        pos += vel
    if pos >= x:
        print(t)
        break
n,m,d,s = tuple(map(int,input().split()))
data = [
    tuple(map(int,input().split()))
    for _ in range(d)
]
sick = [
    tuple(map(int,input().split()))
    for _ in range(s)
]

rotted = [
    [0 for _ in range(s)]
    for _ in range(m+1)
]
for j, (sick_person, sick_time) in enumerate(sick):
    for eat_person, cheese, eat_time in data:
        if sick_person == eat_person and eat_time < sick_time:
            rotted[cheese][j] = 1

ans = 0
for rot_ch in range(1,m+1):
    if sum(rotted[rot_ch]) == s:
        people = [0 for _ in range(n+1)]
        for eat_person, cheese, eat_time in data:
            if cheese == rot_ch:
                people[eat_person] = 1
        ans = max(ans, sum(people))    

print(ans)
n = int(input())

scores = []
curr_a, curr_b, curr_c = 0, 0, 0
for _ in range(n):
    c, s = input().split()
    s = int(s)
    if c == 'A':
        curr_a += s
    elif c == 'B':
        curr_b += s
    else:
        curr_c += s
    scores.append((curr_a,curr_b,curr_c))


def honor(a,b,c):
    does_a_win = 1 if a>=b and a>=c else 0
    does_b_win = 2 if b>=a and b>=c else 0
    does_c_win = 4 if c>=a and c>=b else 0
    return does_a_win + does_b_win + does_c_win


honors = [7] + [ honor(a,b,c) for a,b,c in scores ]

ans = 0
for i in range(n):
    if honors[i] != honors[i+1]:
        ans += 1

print(ans)
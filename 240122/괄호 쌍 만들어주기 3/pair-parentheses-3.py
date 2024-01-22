def count_right(string):
    cnt = 0
    for elem in string:
        if elem == ')':
            cnt += 1
    return cnt 

string = input()
ans = 0
for i in range(len(string)):
    if string[i] == '(':
        ans += count_right(string[i+1:])

print(ans)
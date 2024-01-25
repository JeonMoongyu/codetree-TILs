x,y = tuple(map(int,input().split()))


def is_palindrome(n):
    n_list = list(map(int,list(str(n))))
    return n_list == n_list[::-1]


ans = 0
for num in range(x,y+1):
    if is_palindrome(num):
        ans += 1
print(ans)
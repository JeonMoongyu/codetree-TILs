n, k, t_str = input().split()
n, k = int(n), int(k)


def is_start_t(word):
    for i in range(len(t_str)):
        if word[i] != t_str[i]:
            return False
    return True


t_arr = []
for _ in range(n):
    word = input()
    if is_start_t(word):
        t_arr.append(word)

t_arr.sort()
print(t_arr[k-1])
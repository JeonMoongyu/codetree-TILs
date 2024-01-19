n, k, t_str = input().split()
n, k = int(n), int(k)


def is_start_t(word):
    if len(word) < len(t_str):
        return False
    return word[:len(t_str)]==t_str


t_arr = []
for _ in range(n):
    word = input()
    if is_start_t(word):
        t_arr.append(word)

t_arr.sort()
print(t_arr[k-1])
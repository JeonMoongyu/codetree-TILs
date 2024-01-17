str1 = input()
str2 = input()

def f():
    l1 = len(str1)
    l2 = len(str2)
    for i in range(l1-l2+1):
        if str1[i] == str2[0]:
            satisfied = True
            for j in range(l2):
                if str1[i+j] != str2[j]:
                    satisfied = False
            if satisfied:
                return i
    return -1


print(f())
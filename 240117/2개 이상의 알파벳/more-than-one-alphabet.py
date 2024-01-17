def is_wanted(string):
    for i in range(len(string)):
        for j in range(i+1,len(string)):
            if string[i] != string[j]:
                return True
    return False


string = input()
if is_wanted(string):
    print("Yes")
else:
    print("No")
def is_wanted(string):
    for elem in string[1:]:
        if elem != string[0]:
            return True
    return False


string = input()
if is_wanted(string):
    print("Yes")
else:
    print("No")
def f(string):
    f_string = ""
    for char in string[::-1]:
        f_string += char
    return f_string

string = input()
if string == f(string):
    print("Yes")
else:
    print("No")
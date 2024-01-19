class Character:
    def __init__(self, account=0, level=0):
        self.account = account
        self.level = level

char1 = Character("codetree", 10)
a,l = input().split()
char2 = Character(a, int(l))

print("user", char1.account, "lv", char1.level)
print("user", char2.account, "lv", char2.level)
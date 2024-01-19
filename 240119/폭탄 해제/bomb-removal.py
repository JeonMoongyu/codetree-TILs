class Heje:
    def __init__(self, code=0, color=0, sec=0):
        self.code = code
        self.color = color
        self.sec = sec


code, color, sec = input().split()
heje1 = Heje(code, color, int(sec))
print("code :", heje1.code)
print("color :", heje1.color)
print("second :", heje1.sec)
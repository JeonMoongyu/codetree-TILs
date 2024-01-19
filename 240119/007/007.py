class Mission:
    def __init__(self, code, point, time):
        self.code = code
        self.point = point
        self.time = time

c, p, t = input().split()
mission1 = Mission(c,p,t)
print("secret code :", mission1.code)
print("meeting point :", mission1.point)
print("time :", mission1.time)
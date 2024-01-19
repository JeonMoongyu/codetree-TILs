class Climate:
    def __init__(self, date=0, day=0, weather=0):
        self.date = date
        self.day = day
        self.weather = weather


def sooner(a,b):
    a = tuple(map(int,a.split("-")))
    b = tuple(map(int,b.split("-")))
    return a<b

n = int(input())

data_rain = []
for _ in range(n):
    date, day, weather = input().split()
    if weather == "Rain":
        data_rain.append(Climate(date,day,weather))

idx = 0
for i in range(1,len(data_rain)):
    if sooner(data_rain[i].date, data_rain[idx].date):
        idx = i

ans = data_rain[idx]
print(ans.date, ans.day, ans.weather)
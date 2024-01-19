class Climate:
    def __init__(self, date=0, day=0, weather=0):
        self.date = date
        self.day = day
        self.weather = weather

n = int(input())

ans = Climate("9999-99-99",0,0)
for _ in range(n):
    date, day, weather = input().split()
    if weather == "Rain" and date < ans.date:
        ans = Climate(date,day,weather)

print(ans.date, ans.day, ans.weather)
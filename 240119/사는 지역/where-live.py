class Address:
    def __init__(self, name=0, num=0, area=0):
        self.name = name
        self.num = num
        self.area = area

n = int(input())
arr = [
    input().split()
    for _ in range(n)
]
people = [
    Address(name,num,area)
    for name,num,area in arr
]

idx = 0
for i in range(1,n):
    if people[i].name > people[idx].name:
        idx = i

person = people[idx]
print("name", person.name)
print("addr", person.num)
print("city", person.area)
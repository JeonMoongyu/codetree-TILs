class Address:
    def __init__(self, name=0, num=0, area=0):
        self.name = name
        self.num = num
        self.area = area

n = int(input())
people = []
for _ in range(n):
    name, num, area = input().split()
    people.append(Address(name,num,area))

idx = 0
for i in range(1,n):
    if people[i].name > people[idx].name:
        idx = i

person = people[idx]
print("name", person.name)
print("addr", person.num)
print("city", person.area)
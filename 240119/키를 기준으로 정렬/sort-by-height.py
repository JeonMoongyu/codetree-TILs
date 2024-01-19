class Physical:
    def __init__(self,name=0,height=0,weight=0):
        self.name = name
        self.height = height
        self.weight = weight

n = int(input())
arr = [
    input().split()
    for _ in range(n)
]
people = [
    Physical(name,int(height),int(weight))
    for name,height,weight in arr
]

people.sort(key=lambda x: x.height)
for person in people:
    print(person.name, person.height, person.weight)
class A:
    def __init__(self, name=0, height=0, weight=0):
        self.name = name
        self.height = height
        self.weight = weight

people = []
for _ in range(5):
    n, h, w = input().split()
    people.append(A(n,int(h),float(w)))

people.sort(key = lambda x: x.name)
print("name")
for person in people:
    print(person.name, person.height, person.weight)
print()

people.sort(key = lambda x: -x.height)
print("height")
for person in people:
    print(person.name, person.height, person.weight)
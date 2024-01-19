class Student:
    def __init__(self, height=0, weight=0, num=0):
        self.height = height
        self.weight = weight
        self.num = num

n = int(input())
students = []
for i in range(1,n+1):
    h,w = tuple(map(int,input().split()))
    students.append(Student(h,w,i))

students.sort(key = lambda x: (x.height, -x.weight))
for student in students:
    print(student.height, student.weight, student.num)
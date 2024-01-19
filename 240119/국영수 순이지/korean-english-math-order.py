class Student:
    def __init__(self, name=0, kor=0, eng=0, mat=0):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.mat = mat

n = int(input())
students = []
for _ in range(n):
    name, kor, eng, mat = input().split()
    students.append(Student(name,int(kor),int(eng),int(mat)))

students.sort(key = lambda x: (-x.kor, -x.eng, -x.mat))
for student in students:
    print(student.name, student.kor, student.eng, student.mat)
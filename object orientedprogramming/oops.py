class student:
    def __init__(self,name,rollno,course):
        self.name=name
        self.rollno=rollno
        self.course=course
    def print_student(self):
        print(self.name,self.rollno,self.course)

p1=student("priyanka","48","python")
p1.print_student()

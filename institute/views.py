class course:
    course_name:str
    course_status:bool
    def add_course(self,**kwargs):
        self.course_name=kwargs.get("course_name")
        self.course_status=kwargs.get("course_status")
    def __str__(self):
        return self.course_name

class batch:
    Course:course
    batch_code:str
    start_date:str
    def add_batch(self,**kwargs):
        self.Course=kwargs.get("Course")
        self.batch_code=kwargs.get("batch_code")
        self.start_date=kwargs.get("start_date")
    def __str__(self):
        return self.batch_code

class student:
    student_name:str
    gender:str
    rol:str
    Batch:batch
    def add_student(self,**kwargs):
        self.student_name=kwargs.get("student_name")
        self.gender=kwargs.get("gender")
        self.rol=kwargs.get("rol")
        self.Batch=kwargs.get("Batch")
    def __str__(self):
        return self.student_name
django=course()
django.add_course(course_name="django",course_status=True)
print(django)
db1=batch()
db1.add_batch(Course=django,batch_code="djmay2k22",start_date="18-05-2022")
print(db1)
priyanka = student()
priyanka.add_student(student_name="priyanka",gender="F",rol="48",Batch=db1)
print(priyanka)
print(priyanka.Batch.Course.course_name)
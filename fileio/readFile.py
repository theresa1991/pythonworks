#f=open("abc.txt","w")
#out=[line.rstrip("\n") for line in f]#its a constructor object creation
#print(out)
#company_name="luminar"
#f.write(company_name)
#lst=["a","b","c","d"]
#for aplha in lst:
#    aplha+="\n"
#    f.write(aplha)
students=open("students.txt")
all_students=[stud.rstrip("\n") for stud in students]
fail_students=open("failed.txt")
failed_students=[fail.rstrip("\n")for fail in fail_students]
passed_student=open("passed.txt","w")
passed=set(all_students)-set(failed_students)
print(passed)
for st in passed:
    st+="\n"
    passed_student.write(st)

class employee:
    employ_id:int
    emplop_name:str
    employ_role:int
    def __init__(self,**kwargs):
        self.employ_id=kwargs.get("employ_id")
        self.employ_name=kwargs.get("employ_name")
        self.employ_role=kwargs.get("employ_role")
    def __str__(self):
        return self.employ_name

class department():
    def __init__(self,**kwargs):
        user=kwargs.get("user")#object of employee is passed its contains employ_role
        if user.employ_role=="admin":

            self.depart_name=kwargs.get("depart_name")
            self.user=kwargs.get("user")
        else:
            print("not accesible")

    def __str__(self):
        return self.depart_name
employee=employee(employ_id="1001",employ_name="priyanka",employ_role="admin")#manager
department=department(depart_name="management",user=employee)
print(department)

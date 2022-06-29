class luminar(object):
    id:int
    name:str
    role:str
    def __init__(self,*args,**kwargs):
        self.id=kwargs.get("id")
        self.name=kwargs.get("name")
        self.role=kwargs.get("role")
    def __str__(self):#class object is parent there str returns only object name so create a child and we are overriding it to create our own output
        return self.name
user=luminar(id=1001,name="priyanka",role="manager")
print(user)

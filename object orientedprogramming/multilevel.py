class p1:
    def m1(self):
        print("inside m1")
#class p2(p1):multilevel
class p2:
    def m2(self):
        print("inside m2")
#class p3(p2):multilevel
class p3(p2,p1):
    def m3(self):
        print("inside m3")
pp3=p3()
pp3.m3()
pp3.m2()
pp3.m1()
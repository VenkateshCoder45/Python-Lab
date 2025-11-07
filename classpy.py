class employee:
    #constructor
    def __init__(self,name,empid,salary):
        self.name=name
        self.empid=empid
        self.salary=salary
    def removesalary(self):
        del self.salary
        print(e1.__dict__)

e1=employee("Mahith","CS219",7)
e2=employee("Venkat","CS318",45)
e3=employee("Annaw","CS078",18)
print(e1.__dict__)
e1.removesalary()
class student:

  def __init__(self,name,age,marks):
   self.name=name
   self.age=age
   self.marks=marks

  def display(self):
    print("Hello I am : ",self.name)
    print("My age is : ",self.age)
    print("My Marks are : ",self.marks)

s=student('Srinu',17,80)
s.display()
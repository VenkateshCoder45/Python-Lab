class Test:
    def __init__(self, name, rollno, branch):
        self.name = name
        self.rollno = rollno
        self.branch = branch

        print("Hello, I am:", self.name)
        print("Roll No:", self.rollno)
        print("Branch:", self.branch)
        print()


student1 = Test('Mahi', 219, 'CSE')
student2 = Test('Venkat', 318, 'CSE')


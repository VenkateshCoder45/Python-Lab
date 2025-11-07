class A:
    def sound(self):
        print("Method A")
class B:
    def methodB(self):
        print("Method B")
class C(A,B):
       pass
c=C()
c.methodA()
c.methodB()
                        
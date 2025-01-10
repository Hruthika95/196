class A:
    def apple(self):
        print("Method in class A")

# Parent Class 2
class B(A):
    def apple(self):
        print("Method in class B")
        super().apple()

# Child Class
class C(B):
    def apple(self):
        print("Method in class C")
        super().apple()

# Creating an object of class C
obj = C()
obj.apple()
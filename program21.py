# #INHERITANCE


# #1.

# class Demo():
#     def __init__(self):
#         print("In Demo")

#     def exxtras(self):
#         print("In Demo Extraaaaaaa")

# class Memo(Demo):
#     pass

# obj=Memo()
# obj.exxtras()


# #2.

# class Sky():
#     def __init__(self):
#         print("In Sky")
#         self.x=10
#         self.y=20
#         self.z=30

#     def disresult(self):
#         print(self.x)
#         print(self.y)
#         print(self.z)

#     def C2W(self):
#         print(self.x + self.y)
#         print(self.x * self.z)
#         print(self.z - self.y)

# class Cloud(Sky):
    
#     def __init__(self):
#         print("In Cloud")
#         self.x=50
#         self.y=60
#         self.z=70

# obj= Cloud()
# obj.disresult()
# obj.C2W()



#3.

class Parent:
    a=50
    b=60

    def __init__(self):
        print("In Parent Constructor")

    def othmet(self):
        print("In Parent Method")

    @classmethod
    def impmethod(cls):
        print("In class method")
        print(cls.a+cls.b)

    @staticmethod
    def limpmethod():
        print("In static method")
        print(Parent.b - Parent.a)


class Relative(Parent):
    def __init__(self):
        print("In Relative Constructor")

    def limpmethod(self):
        print("In Relative ")


obj=Relative()
obj.limpmethod()
obj.impmethod()

































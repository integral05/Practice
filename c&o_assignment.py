# #1.Create a Class Human with instance attributes(including variables(name,age) and methods(information)), create the object of the class pass the name and age attributes to the object and access the variables in the method information().

# class Human:

#     def __init__(self,name,age):
#         print("In Demo Constructor")
#         self.name=name
#         self.age=age

#     def information(self):
#         print("Name is: ",self.name)
#         print("Age is: ",self.age)

# name = input("Enter name : ")
# age = int(input("Enter age : "))

# if __name__=="__main__":
#     obj1 = Human(name,age)
#     obj1.information()




# #2. Create a Vehicle class with variables brand, model, year, speed and methods accelerate, brake, honk. Create the child class of vehicle class which overrides the accelerate and honk method. Create the Vehicle class object and pass the attribute to the obj, same create the child class object and pass the same attribute to the child class object.

# class Vehicle:

#     def __init__(self,brand,model,year,speed):
#         print("In Vehicle Constructor")
#         self.brand=brand
#         self.model=model
#         self.year=year
#         self.speed=speed

#     def accelerate(self):
#         print("In Vehicle Accelerate")

#     def brake(self):
#         print("In Vehicle Brake")

#     def honk(self):
#         print("In Vehicle Honk")

# class Child(Vehicle):
#     def accelerate(self):
#        print("Child Acclerate")

#     def honk(self):
#        print("Child Honk")
         
# objV=Vehicle("MET",1265,2010,750)

# objC= Child("MET",1265,2010,750)



# #3. Create the Parent have the @classmethod, @staticmethod, and instance method, and call all these functions by creating the object of a child class.

# class Parent:

#     def __init__(self):
#         print("In Parent Constructor")

#     @classmethod
#     def impmethod(cls):
#         print("In Class Method")

#     @staticmethod
#     def limpmethod():
#         print("In Static Method")

#     def simplemethod(self):
#         print("In Instance Method")

# class Child(Parent):
#     pass

# obj=Child()
# obj.limpmethod()
# obj.impmethod()
# obj.simplemethod()



# #4. Create one parent class with the attribute methods and instance variable, write the same method in the child class, make the object of the child class, call the method, and write the output.

# class Parent:
#     def __init__(self):
#         print("In Parent Constructor")
#         self.x=10
#         self.y=20
#         self.z=30

#     def amethod(self):
#         print("In Parent Method")
#         print(self.x)

#     def bmethod(self):
#         print("In Parent 2 Method")
#         print(self.y)

# class Child(Parent):
#     def amethod(self):
#         print("In Child Method")
#         print(self.x)

#     def bmethod(self):
#         print("In Child 2 Method")
#         print(self.y)

# obj=Child()
# obj.amethod()
# obj.bmethod()




#5. Write a real-time example of Cricket that describes the inheritance

class ICC:
    def __init__(self):
        self.x="Test"
        self.y="ODI"
        self.z="T20"

    def dis(self):
        print("Cricket has :")
        print(self.x)
        print(self.y)
        print(self.z)

class BCCI(ICC):
    pass

obj=BCCI()
obj.dis()



#6. WAP for following MRO with flow diagram [<class '__main__.E'>, <class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B,C):
    pass

class E(D):
    pass

print(E.mro())


    






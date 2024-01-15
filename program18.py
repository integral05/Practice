#Constructor
'''
class Employee():

    def __init__(self,EId,EName):          #CONSTRUCTOR
        print("In Constructor")
        self.EId=EId                       #Instance Variable
        self.EName=EName                   #Instance Variable

    def dispData(self):                    #Instance Method
        print(self.EId)
        print(self.EName)

obj=Employee(2023,"Yash")
obj1=Employee(2025,"Ram")
obj.dispData()
obj1.dispData()
'''

'''
#Class & Static Variables

class Company:
    compName="Biencaps"                   #Class Variable 

    def __init__(self):
        print("In Constructor")
        self.x=10
        self.y=20
        self.z=30

    def compInfo(self):
        print(self.compName)                 #can be call by method/object; because class variables can be access by methods
        print(Company.compName)              #also call by class name
        print("Total Employee: ",self.z)
        print("Present Employee: ",self.y)
        print("Absent Employee: ",self.x)

obj=Company()
obj.compInfo()
'''

'''
#Methods

class Method:
    v1= 100

    def __init__(self):
        print("in Constructor")
        self.x=200
        self.z=300

    def instmethod(self):                             #It is Instance Method
        print("In Instance Method")
        print(self.v1)
        print(self.x)
        print(self.z)

    @classmethod
    def cmethod(cls):                                 #It is Class Method; in class method we can't access instance variable, only class variables are accessable
        print("In Class Method")
        print(cls.v1)
        #print(cls.x)                                 #Error: AttributeError: type object 'Method' has no attribute 'x'
        #print(cls.z)                                 #Error: AttributeError: type object 'Method' has no attribute 'x'

   

    @staticmethod                                   
    def stmethod():                              
#It is Static Method, this method get seprate namespace in PVM, unlike instance method this method do not get space in object namespace; as we call class first static methods get space before other methods and from this methods we can only call class variable and it's own local variablesbut not instance variables
        print("In Static Method")
        a=500
        print(a)
        print(Method.v1)
        #print(x)                                              #NameError: name 'x' is not defined
        #print(z)

obj=Method()
obj.instmethod()
obj.cmethod()
Method().cmethod
obj.stmethod()
'''




























# class LengthError(Exception):
#     def __init__(self,msg):
#         super().__init__(msg)
      
# class IncorrectPinError(Exception):
#     def __init__(self,msg):
#         super().__init__(msg)
        
# def yono_sbi(username,pin):
#     pinList = [1234,4554,6754,8901,3844,6559,3579,4168,1257,3695,4592,7560,9999,0000]

#     if len(str(pin))!=4:
#         raise LengthError("Length of PIN should be 4 digits only")
#     elif int(pin) not in pinList:
#         raise IncorrectPinError("Incorrect PIN ")
#     else:
#         print("Welcome to YONO SBI \n It's LUNCH BREAK LOGIN AFTER 20 MINUTES")

# def cerdentials():       
#     username=input("Enter your username:")

#     try:
#         pin = int(input("Enter your four digit PIN : "))
#     except ValueError:
#         print("PIN should have Integer values only \n \n ENTER YOUR CREDENTIALS AGAIN")
#         username=input("Enter your username: ")
#         pin = int(input("Enter your four digit PIN : "))

#     try:
#         yono_sbi(username,pin)
#     except LengthError as err:
#         print(err)
#     except IncorrectPinError as err:
#         print(err)

# cerdentials()

# y=['yes','YES','Yes']
# ans=input("DO You Want to Continue Transaction \n Yes or No :")

# if ans in y:
#     cerdentials()
# else:
#     print("Have a Nice Day")






from abc import *

class A(ABC):
    def concreteFunction(self):
        self.x=10
        self.y=20

    @abstractmethod
    def abMethod1(self):
        pass

    @abstractmethod
    def abMethod2(self):
        self.z=30

    
class B(A):
    def abMethod1(self):
        self.p=100
        self.q=200

obj = B()
obj.abMethod1()










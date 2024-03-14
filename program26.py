
##1.

# from threading import *
# from time import sleep

# class Calculator(Thread):
#     def __init__(self,a,b):
#         self.num1 = a
#         self.num2 = b
#         super().__init__()
#         #print(current_thread().name)

#     def add(self):
#         self.sum=self.num1 + self.num2

#     def sub(self):
#         self.difference = self.num1 - self.num2

#     def run(self):
#         print(current_thread().name)
#         self.add()
#         self.sub()

# obj = Calculator(20,10)
# obj.start()
# sleep(1)
# print(obj.sum)
# print(obj.difference)
# print(current_thread().name)



# ##2.  BUILT-IN FUNCTIONS IN MULTI THREADING

# from threading import *
# from time import *

# def demo():
#     print("In DEMO Function")
#     print("Native Id of Demo function is: ",get_native_id())
#     print("Details of Main Thread are: ",main_thread())

# def memo():
#     print("In MEMO Function")
#     print("Native Id of Memo Function is: ",get_native_id())

# t1=Thread(target=demo)
# t2=Thread(target=memo)
# print("Check main thread: ",current_thread().is_alive())
# print("Check Memo thread: ",t1.is_alive())
# t1.start()
# t2.start()
# print("Check Memo thread: ",t1.is_alive())
# print("Currently running threads are: ",enumerate())
# print("Total Count of currently running threads: ",active_count())
# print("Check Memo thread: ",t1.is_alive())


###3. JOIN() METHOD

from threading import * 

def demo():
    for i in range(7):
        print("Core2Web")

def memo():
    for i in range(7):
        print("Biencaps")

t1=Thread(target=demo)
t2=Thread(target=memo)
t1.start()
t1.join()
t2.start()
t2.join()

for i in range(7):
    print("python")




















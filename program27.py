#OCCURING OF RACE CONDITION


# #1.

# from threading import *
# x=100
# lockObj=Lock()
# def add():
#     global lockObj
#     lockObj.acquire()
#     print("In Add Function")
#     global x
#     for i in range(5):
#         x=x+10
#         print(x)
#     lockObj.release()

# def sub():
#     print("In Sub Function")
#     global x
#     for i in range(5):
#         x=x-20
#         print(x)

# t1=Thread(target=add)
# t2=Thread(target=sub)
# t1.start()
# t2.start()



##2.

# from threading import * 
# lockObj = Lock()
# class Bus():
#     def __init__(self,name,availableSeats,l):
#         self.availableSeats=availableSeats
#         self.name=name
#         self.lockObj=l

#     def reservation(self,needSeats):
#         self.lockObj.acquire()
#         print("Available Seats are: ",self.availableSeats)
#         if self.availableSeats>=needSeats:
#             nm=current_thread().name
#             print(f"{needSeats} are allocated to {nm}")
#             self.availableSeats-=needSeats
#         else:
#             print("No seats available")
#         self.lockObj.release()

# obj=Bus("Redbus",2,lockObj)
# t1=Thread(target=obj.reservation,args=(2,),name="Tejas")
# t2=Thread(target=obj.reservation,args=(1,),name="Jay")
# t1.start()
# t2.start()


###3. problems in lock

# from threading import * 
# lockObj = Lock()
# class Bus():
#     def __init__(self,name,availableSeats,l):
#         self.availableSeats=availableSeats
#         self.name=name
#         self.lockObj=l

#     def reservation(self,needSeats):
#         self.lockObj.acquire()
#         print(self.lockObj)
#         self.lockObj.acquire()
#         print(self.lockObj)
#         print("Available Seats are: ",self.availableSeats)
#         if self.availableSeats>=needSeats:
#             nm=current_thread().name
#             print(f"{needSeats} are allocated to {nm}")
#             self.availableSeats-=needSeats
#         else:
#             print("No seats available")
#         self.lockObj.release()
#         self.lockObj.release()


# obj=Bus("Redbus",2,lockObj)
# t1=Thread(target=obj.reservation,args=(2,),name="Tejas")
# t2=Thread(target=obj.reservation,args=(1,),name="Jay")
# t1.start()
# t2.start()



# ####4.  RLOCK

# from threading import * 
# rlockObj = RLock()
# class Bus():
#     def __init__(self,name,availableSeats,l):
#         self.availableSeats=availableSeats
#         self.name=name
#         self.rlockObj=l

#     def reservation(self,needSeats):
#         self.rlockObj.acquire()
#         print(self.rlockObj)                                             ############
#         self.rlockObj.acquire()
#         print(self.rlockObj)                                             ###############
#         print("Available Seats are: ",self.availableSeats)
#         if self.availableSeats>=needSeats:
#             nm=current_thread().name
#             print(f"{needSeats} are allocated to {nm}")
#             self.availableSeats-=needSeats
#         else:
#             print("No seats available")
#         self.rlockObj.release()
#         self.rlockObj.release()


# obj=Bus("Redbus",2,rlockObj)
# t1=Thread(target=obj.reservation,args=(2,),name="Tejas")
# t2=Thread(target=obj.reservation,args=(1,),name="Jay")
# t1.start()
# t2.start()


# ######5. Semaphore

# from threading import *
# from time import sleep

# sObj=Semaphore(3)

# def display(name):
#     sObj.acquire()
#     for i in range(5):
#         print("Hello ",name)
#         sleep(1)
#     sObj.release()

# t1=Thread(target=display,args=('Thread-1',))
# t2=Thread(target=display,args=('Thread-2',))
# t3=Thread(target=display,args=('Thread-3',))
# t4=Thread(target=display,args=('Thread-4',))
# t5=Thread(target=display,args=('Thread-5',))
# t1.start()
# t2.start()
# t3.start()
# t4.start()
# t5.start()



######6. BoundedSemaphore

from threading import *
from time import sleep

bsObj=BoundedSemaphore()

def display(name):
    bsObj.acquire()
    for i in range(5):
        print("Hello ",name)
        sleep(1)
    bsObj.release()
    bsObj.release()

t1=Thread(target=display,args=('Thread-1',))
t2=Thread(target=display,args=('Thread-2',))
t3=Thread(target=display,args=('Thread-3',))
t4=Thread(target=display,args=('Thread-4',))
t5=Thread(target=display,args=('Thread-5',))
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()








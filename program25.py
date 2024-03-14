                                            ## MULTI THREADING

# import threading,os

# class Demo:
#     def gun(self):
#         print("Tejas")
#         print(os.getpid())
#         print(threading.current_thread())
#         print(threading.current_thread().name)
#         print(threading.current_thread().ident)
#         print(threading.current_thread().is_alive())



# obj=Demo()
# obj.gun()


# #2.

# from threading import *

# def display():
#     print("In Display Function")
#     print("Thread name is: ",current_thread().name)
#     for i in range(5):
#         print("Core2Web")

# t1= Thread(target=display)
# t1.start()
# print("Thread name is: ", current_thread().name)


# #3.

# from threading import *

# def mun(n,msg):
#     print("In Mun Function")
#     print("Thread name is: ",current_thread().name)
#     for i in range(n):
#         print(msg)

# t1 = Thread(target=mun,args=(10,"Biencaps"))
# t1.start()
# print("Thread name is: ", current_thread().name)


# #4.

# from threading import *

# def mun(n):
#     print("In Mun Function")
#     print("Thread name is: ",current_thread().name)
#     for i in range(n):
#         print("Single Argument")

# t1 = Thread(target=mun,args=(10,))
# t1.start()
# print("Thread name is: ", current_thread().name)


#5.

from threading import *

def mun(n,msg):
    print("In Mun Function")
    print("Thread name is: ",current_thread().name)
    for i in range(n):
        print(msg)

t1 = Thread(target=mun,kwargs={"n":10,"msg":"Hello"})
t1.start()
print("Thread name is: ", current_thread().name)



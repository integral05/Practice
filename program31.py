### Daemon Thread

##1. Daemon Nature of Main Thread

# from threading import * 
# print("Hello")
# obj = current_thread()
# print("Daemon Nature of Main Thread is: ",obj.daemon)


##2. To change daemon nature of thread

# from threading import *
# def display():
#     print("In Display Function")
#     t2 = Thread(target=demo)
#     print("Daemon Nature of t2 Thread after change is: ",t2.daemon)

# def demo():
#     print("In Demo Function")

# t1 = Thread(target=display)
# print("Daemon Nature of t1 Thread is: ",t1.daemon)
# t1.daemon=True
# print("Daemon Nature of t1 Thread after change is: ",t1.daemon)
# t1.start()











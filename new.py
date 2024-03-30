from threading import *

class MyThread (Thread):
    def __init__(self,x,y):
        Thread.__init__(self)
        self.x=x    
        self.y=y
            
    def run(self):
            print('In Run Method')
            print(current_thread().name)
            print(self.x)
            print(self.y)
            
t1=MyThread(10,20)
t1.run() 

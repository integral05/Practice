# ##1. Thread Communication

# from threading import *
# from time import sleep

# eventObj=Event()

# def task():
#     print("Game has started")
#     sleep(11)
#     eventObj.set()

# def end():
#     eventObj.wait()
#     if eventObj.is_set():
#         print("Game Ended")

# t1=Thread(target=task)
# t2=Thread(target=end)

# t1.start()
# t2.start()



###2.

from threading import *
from time import sleep

eventObj=Event()
class rFile(Thread):

    def readFile(self):
        print("Reading File")
        with open("C:/Python Programs/GITHUB/Practice/p27file.txt","r") as fileObj:
            self.lines=fileObj.readlines(5)
            eventObj.set()

    def run(self):
        self.readFile()


def writeFile(lines):
    eventObj.wait()
    if eventObj.is_set():
        print("Writing File")
        with open("newFile.txt","w+") as fObj:
            fObj.writelines(lines)

obj=rFile()
#t1=Thread(target=obj)
obj.run()
t2=Thread(target=writeFile,args=(obj.lines,))
t2.start()

















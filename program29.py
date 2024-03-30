## THREAD COMMUNICATION USING CONDITION CLASS

import threading
import time

def write_temp():
    con.acquire()
    with open("report.txt","w") as f1:
        days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
        for day in days:
            temp = input(f"Enter the temperature for {day}: ")
            f1.write(temp + "\n")
    con.notify_all()
    con.release()


def max_temp():
    con.acquire()
    con.wait()
    with open("report.txt","r") as f2:
        data = f2.readlines()
        max = 0
        for temp in data:
            temp = float(temp.strip("\n"))
            if temp>max:
                max=temp
        print("Maximum temperature of week is: ",max)
        con.release()

def avg_temp():
    pass

con = threading.Condition()
t1 = threading.Thread(target=write_temp)
t2 = threading.Thread(target=max_temp)
t3 = threading.Thread(target=avg_temp)
t1.run()
t2.run()
t3.run()



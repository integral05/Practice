### Thread communication using Queue Object


from threading import Thread
from queue import Queue

def producer (my_que):
    print("Producer Started")
    n = int(input("Enter number students: "))
    for i in range(n):
        marks = float(input("Enter marks: "))
        my_que.put(marks)
    my_que.put(None)
    print("Producer Stopped")

def consumer(my_que
             ):
    print("Consumer Started")
    while True:
        value = my_que.get()
        if value is None:
            break
        print(f"Got {value}")
    print("Consumer Stopped")


my_que = Queue()
t1 = Thread(target=producer,args=(my_que,))
t2 = Thread(target=consumer,args=(my_que,))
t1.start()
t2.start()




#GENERATOR

'''
def fun():
    x=10
    yield x
    x=x+1
    yield x

    print("stop")
for i in fun():
    print(i)
'''

'''
def fun2():
    print("Start fun")
    yield 10
    yield 20
    yield 30
    yield 40
    print("End fun")

ret=fun2()
print(next(ret))
print(next(ret))
print(next(ret))
print(next(ret))
'''


'''
def fun3(x,y):
    print("Sart fun")
    while(x<=y):
        yield x
        x+=1
    print("End fun")

for i in fun3(1,10):
    print(i)
'''



def fun4():
    print("Start Fun")
    x=100
    yield x
    p=90
    yield p
    print("End Fun")
    yield

ret= fun4()
print(next(ret))
print(next(ret))



















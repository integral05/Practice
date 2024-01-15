'''
def outerfun():
    print("IN OUTER FUNCTION")

    def innerfun():
        print("IN INNER FUNCTION")

    innerfun()
outerfun()
'''
'''
def outerfun():
    print("in outer function")

    def innerfun():
        print("in inner function")

    return innerfun
ret=outerfun()
ret()
'''
'''
def outer(x,y):
    def inner(a,b):
        print("in inner function")
        return a+b
    print("in outer function")
    print(x+y)
    return inner
retobj= outer(5,8)
innerRet=retobj(3,4)
print(retobj)
'''

''' 
def outer():
    def inner1(x,y):
        print("IN INNER1 FUNCTION")
        return x+y

    def inner2(a,b):
        print("IN INNER2 FUNCTION")
        return a+b

    return inner1,inner2
in1,in2=outer()
ret1=in1(10,20)
ret2=in2(3,4)
print(ret1 + ret2)
print(in1)
print(in2)
'''


















































































































#Decorator

# There are two types of Decorator i.e. 1. class decorator (ex: @class method and @static method) seen in classes and object, 2. function decorator ; we will understand fun. decorator


# Passing function as Parameter
'''
def fun1():
    print("In fun1")

def fun2(fun):
    print("In fun2")
    fun()

fun2(fun1)



#Creating Decorator Function

def outerfun(fun):                                              #fun=address of simplefun

    def inner1():
        print("Start Functioning")
        fun()                                                   #4.fun() contains address of simplefun() so it calls simplefun
        print("End Functioning")

    return(inner1)                                              #returns address of inner1 fun 

def simplefun():
    print("Perform Tasks")

simplefun=outerfun(simplefun)                                   #1.calls outerfun passing simplefun as parameter, 2.stores returned address in simplefun
simplefun()                                                     #3.here simplefun() contains address of inner1 fun so it directly calls inner1 



def decorfun(fun):

    def wrapper():
        print("Start Wrapping")
        fun()
        print("End Wrapping")
    
    return wrapper


@decorfun
def normalfun():
    print("It's secret")

normalfun()
'''



#Normal Function having parameter
def decorfun(fun):

    def wrapper(*args):
        print("Start Machine")
        fun(*args)
        print("Stop Machine")

    return wrapper

@decorfun
def normalfun(x):
    print("Printing Paper in:",x)

a=2024
normalfun(a)

































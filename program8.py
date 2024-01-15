
'''
def fun(x,y,z=30):
    print(x)
    print(y)
    print(z)

fun(10,20,40)
'''
'''
def fun(x=30,y,z):
    print(x)
    print(y)
    print(z)

fun(10,20,40)
'''
'''
def fun(*argv):
    for i in argv:
        print(i,end=" ")
    print()

fun(1,2,3,4,5,6,7,8,9,10)
'''
'''
def fun(x,y,*argv):
    print(x)
    print(y)
    print(argv)
    print(type(argv))
fun(1,2,3,4,5,6,7,8)
'''

def fun(x,y,**argv):
    print(x)
    print(y)
    print(argv)
    print(type(argv))

fun(x=3,y=2,z=6)




























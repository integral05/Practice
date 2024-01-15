'''
def fun(a,b):
    print("Sum of given values is:",a+b)

a=int(input("Enter value for a:"))
b=int(input("Enter value for b:"))

fun(a,b)



def fun2(x):
    fact=1
    for i in range(1,x+1):
        fact=fact*i

    return fact

num=int(input("Enter your number:"))
print("Factorial is:",fun2(num))



def fun3(x,y):
    a=x+y
    b=x-y
    c=x*y
    d=x/y

    return a,b,c,d

x=int(input("Enter value for x:"))
y=int(input("Enter value for y:"))
result=fun3(x,y)
'''
#print("Addition is:",result[0])
#print("Subtraction is:",result[1])
#print("Multiplication is:",result[2])
#print("Division is:",result[3])























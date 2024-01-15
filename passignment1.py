
# def fun():
#     print("in fun")

# if __name__=='__main__':
#     fun()



##1.

# def add(x):
#     def inner(y):
#         return x * y
#     return inner 

# if __name__=='__main__':
#     add_3=add(3)
#     result=add_3(7)
#     print(result)



# #2.

# def outer():
#     def inner():
#         return "Greetings from the inner function!"
    
#     return inner()

# if __name__=="__main__":
#     result=outer()
#     print(result)



# #3.

# def outer():
#     def inner():
#         return "This is the inner function."
    
#     return inner

# if __name__=="__main__":
#     retObj=outer()
#     retInner = retObj()
#     print(retInner)



# #4.

# def outer():
#     def inner():
#         return outer
    
#     return inner

# if __name__=="__main__":
#     retObj=outer()
#     retInner = retObj()
#     print(retInner)



# #5.

# def outer():
#     def inner(outer):
#         print(outer)
#         return inner
#     return inner(outer)

# if __name__=="__main__":
#     retObj = outer()
#     print(retObj)



# #6.

# def outer():
#     def inner1(a,b):
#         print("In Inner1")
#         return a - b
    
#     def inner2(obj):
#         print("In inner2")
#         print(obj)
#         return inner2
    
#     retInner1 = inner1(10,4)
#     retInner2= inner2(retInner1)
#     return retInner2

# if __name__=="__main__":
#     retObj = outer()
#     print(retObj)



# #7.

# def outer():
#     def inner():
#         return "Hello, Core2web!"
#     return inner
#     print("In Outer Function")

# if __name__== "__main__":
#     result = outer()()
#     print(result)



# #8.

# def outer():
#     message = "I am the outer function."
#     def inner():
#         return message
#     return inner

# if __name__=="__main__":
#     inner_function = outer()
#     result = inner_function()
#     print(result)



# #9.

# def outer():
#     count=0

#     def inner():
#         nonlocal count
#         count+=1
#         return count
#     return inner

# if __name__=="__main__":
#     counter= outer()
#     print(counter())
#     print(counter())



#10.

def outer(flag):
    def inner():
        return "This is true." if flag else "This is false."
    
    return inner

if __name__== "__main__":
    true_function = outer(True)
    false_function=outer(False)

    print(true_function())
    print(false_function())






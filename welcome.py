'''DECORATOR'''

'''Basic Decorator:
Create a decorator that prints a message before and after the execution of a function. Apply this decorator to a sample function to demonstrate its functionality.'''


# def decor(fun):

#     def innerfun():
#         print("Start Process")
#         fun()
#         print("End Process")

#     return innerfun

# @decor
# def normalfun():
#     print("Currently You are in Process")

# # normalfun=decor(normalfun)                  #if you don't use @decor then to call decor() we can use this line
# normalfun()



'''function with parameter is passed as parameter to decorator'''

# def decorfun(func):

#     def wrapperfun(a):

#         print("Print Paper")
#         func(a)
#         print("Stop Print")

#     return wrapperfun

# @decorfun
# def paper(a):
#     print("Total count is:",a)

# paper(100)



# total=75

# def decor1(fun1):

#     def count(*args):
#         print("Absent students are:")
#         fun1(*args)
#         print("Present Count is:",total-len(args))
#         print("Absent Count is:",len(args))

#     return count

# @decor1
# def absent(*args):
#     print("Roll No. are:")
#     for i in args:
#         print(i)


# absent(1,7,9,10,15,25,29,36,45,58,69,71)



# def outerfun(func):
#     def gift(x):
#         #print("For Purple:1     For Red:2     For Blue:3" )
#         #print()
#         #x=int(input("Enter value of x:"))
#         if(x==1):
#             print("Purple Start")
#             func(x)
#             print("Purple End")

#         elif(x==2):
#             print("Red Start")
#             func(x)
#             print("Red End")

#         elif(x==3):
#             print("Blue Start")
#             func(x)
#             print("Blue End")

#         else:
#              print("Invalid Value")
#     return gift

# @outerfun
# def item(x):
#      print("Birthday Gift")

# print("For Purple:1     For Red:2     For Blue:3\n" )
# x=int(input("Enter value of x:\n"))
# item(x)



# def dec1(fun):

#     def wrap1(*arg):
#         print("You are in starting phase be active")
#         ans=int(input("Have you completed your task 'for yes give 1 and for No give 0':"))
#         if (ans==1):
#             print("You can go to next round")
#             fun(*arg)
#         else:
#             print("You are eliminated")

#     return wrap1


# def dec2(func):

#     def wrap2(*arg):
#         print("You are the GOAT")
#         func(*arg)
#     return wrap2

# @dec2
# @dec1
# def normalfunc(*arg):
#     print("So you have to DIE")

# normalfunc()







    


        

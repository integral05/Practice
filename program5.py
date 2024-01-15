#1
'''
num=int(input("Enter your value:"))
if(num>0):
    print("{} is positive number".format(num))
elif(num<0):
    print("{} is negative number".format(num))
else:
    print("Equals to Zero")
'''

#2
'''
num= int(input("Enter your value:"))
if((num*num)%2==0):
    print(num*num,"is the even square")
else:
    print(num*num,"is the odd square")
'''


#3
'''
num= int(input("Enter the value:"))
i=1
while(num>0):
    print(num)
    num=num-1
'''


#4.else suit
###############################################
'''
charList=['a','e','i','o','u']

char=input("Enter your character:")
for vowel in charList:
    if char==vowel:
        print(char,"is present")

else:
    print(char,"is not present")              
'''
################################################


#5. for loop
'''
num=int(input("Enter your value:"))

for i in range(num):
    if (i%2!=0):
        print(i,end="*")
print()
'''

#6.

num=int(input("Enter your value:"))

for i in range(1,num):
    if(i%3==0):
        print("THREE",end=" ")
    elif(i%5==0):
        print("FIVE",end=" ")
    else:
        print(i,end=" ")
print()








































































































































































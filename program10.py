'''
import array as arr
num= arr.array('i',[1,2,3,4,5,6,7,8,9])
print(num)
'''
'''
import array as arr
num=arr.array('i',[1,3,2,4,23,5,6,7,8,9,98,76,53])
for i in num:
    print(i)
'''

'''
import array as arr
words=arr.array('u',['i','n','t','e','g','r','a','l'])
print(words)
#array('u', 'integral')
'''

#METHODS IN ARRAY
'''
import array as arr

num = arr.array('i',[10,20,30,40,50,60,30,50,20,30,70,80])
print(num)

num.append(90)
print(num)

print(num.buffer_info())

print(num.count(30))
'''
#print(num.extend(90,100,110))
#TypeError: extend() takes at most 1 argument (3 given)
'''
num.extend([90,100,110])
print(num)
'''

'''
list=[11,22,33]
num.fromlist(list)
print(num)
'''
'''
print(num.index(30))
'''

'''
num.insert(4,5)
print(num)
'''

'''
num.pop()
print(num)
num.pop(5)         #requires index of element
print(num)
'''

'''
num.remove(50)
print(num)
'''

'''
num.reverse()
print(num)
'''

'''
list1= num.tolist()
print(list1)
'''



#ARRAY SLICING


import array as arr

num = arr.array('i',[1,2,3,4,5,6,7,8,9,10])
print(num)

for i in num[3::]:
    print(i)














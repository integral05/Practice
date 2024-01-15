#SET 

'''
data=set()
print(data)
print(type(data))
'''

'''
data1={1,2,3,4,5,6,7,8}
print(data1)
'''

'''
data2={0,1,2.3,45.68,"a","Defg"}
print(data2)
'''

'''
data3=set([1,2,3,4,5,65,43,2,2])
print(data3)
'''

'''
data4={1,2,3,4,54,65,76,78,90,12,34,1,3,76}
print(data4)
'''

#access & add value in sets
'''
data5={1,2,3,4,5,6}
#print(data5[3])                     #Error:

#data5[3]=30                         #Error:
print(data5)
'''

'''
data6={1,2,3,4,5,6}
print(data6)

data6.add(7)
print(data6)
'''


#Frozen Set

data7=frozenset([1,2,3,4,5,6,45,43,67,32,12,98,65,0,90])
print(data7)
#data7.add(7)                                   #Error because in frozen set do not allowed operations on it, as they are immutable
print(data7)































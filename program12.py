#Methods in Set
set1={4,7,5,8,6,9,0}
data={1,2,3,4,5,6}
print(data)
print(set1)
print("Set after using method:")

#add()
'''
data.add(7)
print(data)
'''


#copy() ---------shallow copy
'''
data2=data.copy()
print(data)
print(data2)
'''


#difference()      return the diff. of 2 or more sets in a new set
'''
data3={5,7,8,9,0,3,4}
set3=data3.difference(data)                         #way 1
set4=data-data3                                     #way 2
print(set3)
print(set4)
'''


#difference_update                  
'''
data4={3,6,4,7,8,9,0}
data.difference_update(data4)
print(data)
'''


#discard()
'''
data.discard(3)
print(data)
'''


#intersection()
'''
data5=data.intersection(set1)
print(data5)
'''


#intersection_update()
'''
data.intersection_update(set1)
print(data)
set1.intersection_update(data)
print(set1)
'''


#isdisjoint()        return True if two sets have a null intersection
'''
print(data.isdisjoint(set1))
set2=(7,8,9,0)
print(data.isdisjoint(set2))
'''


#issubset()
'''
print(data.issubset(set1))
'''


#issuperset()
'''
print(data.issuperset(set1))
'''


#symmetric_difference()      returns the symmetric diff. of 2 sets in a new set
'''
data8=data.symmetric_difference(set1)
print(data8)
'''


#symmetric _difference_update()      returns the symmetric diff. of 2 sets in a same set
'''
data.symmetric_difference_update(set1)
print(data)
'''


#union()
'''
data9=data.union(set1)
print(data9)
'''



#update()
'''
data.update(set1)
print(data)
'''



#pop()
'''
data.pop()
print(data)
'''


#remove()
'''
data.remove(4)
print(data)
'''


#clear()

data.clear()
print(data)




















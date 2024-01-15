#LIST
#CREATING LIST TYPE 1
'''
players=["rohit","virat","sky"]
print(type(players))
print(players)
'''

'''
list1=["Akash",10,50.90]
print(list1)
'''
'''
employee=[{"Rohit":45},{"Virat":18},{"Shubman":60}]
print(employee)
'''

#TYPE 2 -----------> list constructor

'''
score=list()
print(type(score))
print(score)
'''

'''
marks=[10,20,30,40.54,60,78,91,55.12]
avg=list(marks)
print(avg)
print(type(avg))
'''


#TYPE 3---------------> comprehension:-     here we get list by using range 

'''
normlist=[num*num for num in range(1,10)]
print(type(normlist))
print(normlist)
'''

'''
numlist=[i for i in range(1,20)]
print(numlist)
'''


#ACCESSING ELEMENTS FROM LIST


#player=["Rohit","Virat","KLRahul","Shreyas","Shubman"]
#1. BY INDEX
'''
print(player)
print(player[0])
print(player[3])
print(player[4])
print(player[-1])
print(player[-4])
'''


#2. BY SLICING
'''
print(player[2::])                           #["KLRahul","Shreyas","Shubman"]
print(player[2:4:2])                         #["KLRahul"]
print(player[:5:3])                          #["Rohit","Shreyas"]
print(player[::3])                           #["Rohit","Shreyas"]
print(player[4:2:-1])                        #[shubman,shreyas]
print(player[4:2:2])                         #
'''


#METHODS IN LIST
'''
player=["Rohit","Virat","KLRahul","Shreyas","Shubman"]
print(player)
print("LIST AFTER USING METHOD:")

#TO ADD
#1. append()

player.append("SKY")
print(player)



#2 extend()

player.extend(["Jaddu","Bumrah","Shami"])
print(player)


#3. insert() ----------> at particular index

player.insert(3,"Hardik")
print(player)


#TO DELETE 

#1. remove()

player.remove("SKY")
print(player)



#2.pop()
player.pop()
print(player)


#3. clear()

player.clear()
print(player)
'''


#player=['Rohit', 'Virat', 'KLRahul', 'Hardik', 'Shreyas', 'Shubman', 'SKY', 'Jaddu', 'Bumrah', 'Shami']
#print(player)
print("LIST AFTER USING METHOD:")

#4.count()
'''
print(player.count("SKY"))
'''


#5. index()
'''
print(player.index("Jaddu"))
'''


#6. reverse()
'''
player.reverse()
print(player)
'''


#7.sort()
'''
player.sort()
print(player)
'''


#8. copy()------------------>SHALLOW COPY; in shallow copy if we make changes in original list it will affect the another(copied) list also
'''
list2=player.copy()
print(list2)
'''

#NESTED LIST 

'''
lang=["Python","Java","CPP",["Go","Rust","Dart"]]
print(lang)
print(lang[2])
print(lang[3])
print(lang[3][1])
print(lang[3][0])
'''


#SHALLOW & DEEP COPY

#1.SHALLOW COPY
'''
lang=["Python","Java","CPP",["Go","Rust","Dart"]]
print(lang)
newlist=lang.copy()
print(newlist)
lang[3][1]="Javascript"
print(lang)
print(newlist)
'''


#2.SHALLOW COPY

import copy as cp

lang=["Python","Java","CPP",["Go","Rust","Dart"]]
print(lang)
newlist2=cp.deepcopy(lang)
print(newlist2)
lang[3][1]="Javascript"
print(lang)
print(newlist2)








